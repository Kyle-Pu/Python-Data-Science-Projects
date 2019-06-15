# Deep Learning - Convolutional Neural Network Classifier for Fashion MNIST Images
This model is a convolutional neural network that classifies images of clothing items into 10 separate categories as identified by the Fashion MNIST Dataset!

## Setup
Run in the command line:
`pip3 install tensorflow`,
`pip3 install keras`,
`pip3 install numpy`

***Also make sure to unzip fashion-mnist-train.zip into this directory!***

## Technologies Used
1. Tensorflow
2. Keras
3. Convolutional Neural Network
4. Conv2D Layers
5. Dense Layers

## Results
**VERSION 1**
The model's accuracy on the validation set of clothing images is about 91.67%. There is no noticeable improvement of our model's performance after the fifth epoch so, with current settings, it may be more practical to cap our model's training at 5 epochs (to save time and computational resources).

**VERSION 2**
The model's validation set score is now about 86%. Though this performs worse than version 1 of the CNN, it will likely perform better on outside, unseen data since the Droupout layers reduce overfitting. The validation set has similar pictures to the training set so it's likely that the higher validation score for Model 1 is due to a bit of overfitting.

See below for more details on what changed between Version 1 and Version 2!

### Model Settings
**VERSION 1**
1. Loss function is categorical_crossentropy
2. Optimization function is "Adam." See Reference [2].
3. Measuring for accuracy
4. 20 Epochs (Iterations over our dataset)
5. Batch size = 100 (this is important since we don't have to load whole datasets into memory when we use batches)
6. 20% of data taken for validation set

**VERSION 2 (Added Stride Length Adjustment)**
1. Strides = 2 --> this means our filters will be applied every other row and every other column. As a result, function maps will be a quarter of their original size and our model will train much faster!
 
### Convolutional Neural Network Structure by Layer
**VERSION 1**
1. Conv2D Layer, 8 nodes, 3 by 3 sized filter, Relu activation function
2. Conv2D Layer, 24 nodes, 3 by 3 sized filter, Relu activation function
3. Conv2D Layer, 48 nodes, 3 by 3 sized filter, Relu activation function
4. Flatten layer
5. Dense layer, 100 nodes, Relu-activated
6. Prediction layer: Dense layer, 10 nodes (1 for each class of clothing item), Softmax activation (to convert numerical predictions into percentages)

**VERSION 2**
1. Same as above except I added in a Droupout(0.5) layer between each Conv2D layer. This provides regularization, which means that randomly selected neurons will be ignored during training. This regularization helps prevent overfitting because it allows every node's weights to have a magnitude of importance in the final model. By randomly disabling certain node connections during training, no one node can dominate the resulting model (i.e. no node's weight can be so large that the other nodes won't matter anymore). The 0.5 parameter just means that at every update during training, 50% of the input units will be set to 0 (effectively disabling the node since it no longer contributes to the prediction).

*Note:* I added double the amount of nodes per hidden, Conv2D layer in order to capture hierarchical features in the images.

### Model Performance per Epoch
**VERSION 1**
Epoch 1/20 48000/48000 [==============================] - 58s 1ms/sample - loss: 0.4561 - acc: 0.8356 - val_loss: 0.3404 - val_acc: 0.8741 

Epoch 2/20 48000/48000 [==============================] - 59s 1ms/sample - loss: 0.2905 - acc: 0.8942 - val_loss: 0.3002 - val_acc: 0.8895 

Epoch 3/20 48000/48000 [==============================] - 60s 1ms/sample - loss: 0.2272 - acc: 0.9156 - val_loss: 0.2836 - val_acc: 0.8984 

Epoch 4/20 48000/48000 [==============================] - 64s 1ms/sample - loss: 0.1836 - acc: 0.9327 - val_loss: 0.2564 - val_acc: 0.9103 

Epoch 5/20 48000/48000 [==============================] - 61s 1ms/sample - loss: 0.1417 - acc: 0.9478 - val_loss: 0.2521 - val_acc: 0.9167 

***Note: Epochs 6 - 20 exlcuded for brevity and because no meaningful change in the validation accuracy scores occurred.***

**VERSION 2**
Epoch 1/20
48000/48000 [==============================] - 3s 60us/sample - loss: 0.9591 - acc: 0.6518 - val_loss: 0.5913 - val_acc: 0.7870

Epoch 2/20
48000/48000 [==============================] - 3s 61us/sample - loss: 0.6604 - acc: 0.7585 - val_loss: 0.5247 - val_acc: 0.8083

Epoch 3/20
48000/48000 [==============================] - 3s 61us/sample - loss: 0.6056 - acc: 0.7774 - val_loss: 0.4946 - val_acc: 0.8150

Epoch 4/20
48000/48000 [==============================] - 3s 62us/sample - loss: 0.5706 - acc: 0.7910 - val_loss: 0.4598 - val_acc: 0.8338

Epoch 5/20
48000/48000 [==============================] - 3s 63us/sample - loss: 0.5471 - acc: 0.7979 - val_loss: 0.4456 - val_acc: 0.8375

*Epochs 6-14 not included...*

Epoch 15/20
48000/48000 [==============================] - 3s 70us/sample - loss: 0.4566 - acc: 0.8296 - val_loss: 0.3745 - val_acc: 0.8622

Epoch 16/20
48000/48000 [==============================] - 3s 70us/sample - loss: 0.4507 - acc: 0.8310 - val_loss: 0.3689 - val_acc: 0.8638

Epoch 17/20
48000/48000 [==============================] - 3s 69us/sample - loss: 0.4487 - acc: 0.8322 - val_loss: 0.3633 - val_acc: 0.8673

Epoch 18/20
48000/48000 [==============================] - 3s 69us/sample - loss: 0.4430 - acc: 0.8340 - val_loss: 0.3675 - val_acc: 0.8640

Epoch 19/20
48000/48000 [==============================] - 3s 69us/sample - loss: 0.4403 - acc: 0.8362 - val_loss: 0.3616 - val_acc: 0.8671

Epoch 20/20
48000/48000 [==============================] - 3s 70us/sample - loss: 0.4430 - acc: 0.8345 - val_loss: 0.3597 - val_acc: 0.8672

***Note: Each epoch here took only 3 seconds to run versus the first 5 epochs from version 1 of the convolutional neural network, which took about a minute each!!!***

## References
[1] https://keras.io/models/sequential/

[2] https://machinelearningmastery.com/adam-optimization-algorithm-for-deep-learning/

[3] https://keras.io/utils/

[4] https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv2D

[5] https://www.kaggle.com/dansbecker/rectified-linear-units-relu-in-deep-learning

[6] https://www.saama.com/blog/different-kinds-convolutional-filters/

[7] https://stats.stackexchange.com/questions/153531/what-is-batch-size-in-neural-network

[8] https://machinelearningmastery.com/difference-between-a-batch-and-an-epoch/

