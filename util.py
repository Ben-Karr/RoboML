def get_df(df, val_method = 'groups', background = None, val_pct = 0.2,
           angle = None, unique = True, orientation = None, verbose = True):
    df_ok = df[df.usability == 'ok'].copy()

    if angle:
        assert(angle in ['top', 'side']), 'Pick a valid angle'
        if verbose: print('Reduce the dataframe to only {} angle photos'.format(angle))
        df_ok = df_ok[df_ok.angle == angle]

    if orientation:
        assert(orientation in ['L','R']), 'Pick a valid orientation'
        if verbose: print('Reduce the dataframe to only {} oriented photos'. format(orientation))
        df_ok = df_ok[df_ok.orientation == orientation]

    groups = np.array(df_ok.groups.unique())

    if val_method == 'background': # the model is validated on an unseen background
        if verbose: print('Build the validation set by background')
        if background not in df_ok.background.unique():
            background = random.choice(df_ok.background.unique())
            if verbose: print('Pick the background {} at random'.format(background))
        else:
            if verbose: print('Pick the background {}'.format(background))

        is_valid = df_ok.background == background

    elif val_method == 'groups': # the model is validated on unseen groups
        if verbose: print('Building the validation set from groups, picking {}% of the groups at random'.format(val_pct * 100))
        total_groups = len(groups)
        val_no = int(val_pct * total_groups)

        is_valid = df_ok.groups.isin(np.random.choice(groups, val_no))

    else:
        if verbose: print('Pick a valid validation method')
        return None

    df_ok['is_valid'] = is_valid

    if unique: # all instances of a group are considered for validation
        if verbose: print('Reduce the dataframe, so for every group in the training there is only one unique item')
        df_unique = pd.DataFrame(columns = df_ok.columns)
        for group in groups: # in none of the validation methods, a group should appear in both training and validation set
            df_tmp = df_ok[df_ok.groups == group]
            if df_tmp.iloc[0]['is_valid']:
                df_unique = df_unique.append(df_tmp, ignore_index = True)
            else:
                df_unique = df_unique.append(df_tmp.sample(1), ignore_index = True)
        df_ok = df_unique

    print('Total items: {} of which the in validation set: {} '.format(df_ok.shape[0], df_ok.is_valid.sum()))
    return df_ok[['fname','label','is_valid']]

def get_blocks(size, trans_mult = 1.):
    dBlock = DataBlock(blocks = (ImageBlock, CategoryBlock),
                       splitter = RandomSplitter(),#ColSplitter(),
                       get_x = lambda x: f'{im_path}/'+ x.fname,
                       get_y = lambda x: x.label,
                       item_tfms = Resize((640, int(640 * 1.6)), method = 'squash', pad_mode = 'zeros'),
                       batch_tfms = aug_transforms(size = (size, int(size * 1.6)),
                                                   max_rotate = 10.,
                                                   min_zoom = 0.95,
                                                   max_zoom = 1.05,
                                                   p_affine = 0.8,
                                                   p_lighting = 0.8,
                                                   max_lighting = 0.3,
                                                   max_warp = 0.0,
                                                   mult = trans_mult
                                                  )
                      )
    return dBlock

def get_learner(size = 224, bs = None, arch = resnet34):
    if not bs:
        bs = int(64 * 224 / size)

    blks = get_blocks(size)
    df_res = get_df(df,
                    angle = 'side',
                    orientation = None,
                    val_pct = 0.2,
                    val_method = 'background',
                    background = 'black',
                    unique = True,
                    verbose = False)

    dls = blks.dataloaders(df_res, bs = bs)

    return cnn_learner(dls, arch, metrics=accuracy).to_fp16(), dls
