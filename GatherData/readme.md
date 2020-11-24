## Process: ##
1. To have a smaller filesize the images are cropped. The first notebook contains a widget that lets you choose 3 edges of the target photo and carculates the 4th to have a certain width/height ratio. The 4 corners are exported to .csv.
2. Crop the images to the determined size.
3. Create the labels and add them to the .csv. (Most of the labeling was done by drag&drop the images to meaningful folders and extract the label from the foldername.)

## Folder structure: ##

* __models__: The weights of the steps & results of the different architectures
* __data__: Pictures to train the model on \& dataframes containing metadata
  * __pic__:  Pictures to train the model on
    * __crop__: Cropped images, to reduce the Image-size;
    * __src__: Uncropped images;
    * __background__: Samples for each background