## Project Description: ##
This project aims to build a __tool that aids kids in building electronic circuits for robotics__. (Arguably) the most important part of teaching kids robotics (or programming / technologie in general) is to let them build their own robots. However, this goes hand in hand with the hardest part of the learning process: debugging. Taking a lot of time to fix a bug in the electronic circuit is extremely frustrating and there is no skill to lean that makes this easyer, other than experience.

This is less of a problem in a classromm situation, where an experienced instructor can take a look at the circuit and identify the problem. But due to the corona situation the idea (and the desire) came, to have a backup solution, when it is not possible to have human help on site.


## Phases: ##
* Gather Data:
  * Record videos of electronic circuits
  * Label if the circuit is correct or not & where the circuit is broken
  * Split video in individual pictures

* Build Deep Learning Model:
  * Try Transfer Learning for ResNet34/50/DenseNet
  * Try to predict correct vs incorrect and optional position of first error

* Build a Smartphone App (if the DL model works)
