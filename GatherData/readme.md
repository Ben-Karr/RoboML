Folder structure:
* __models__: The weights of the steps & results of the different architectures
* __data__: Pictures to train the model on
  * __pic__:  Pictures to train the model on
    * __crop__: Cropped images, to reduce the Image-size; _on hold_
      * __orig__: Images in the original resolution
    * __sample__: Small subset of 'correct' Images
    * __src__: Uncropped images;
      * __640__: Images; resized to 640 x 1024 pxl
      * __orig__: Images in the original resolution
  * __vid[old]__: Test; try to split the videos into pictures for easy generation of training material; not successful
    * __correct__: Images with label correct
    * __incorrect__: Images with label incorrect
    * __sample__: Small subset of the correct folder

```flow {theme = 'hand'}
Andrew -> China: Says Hello
```
