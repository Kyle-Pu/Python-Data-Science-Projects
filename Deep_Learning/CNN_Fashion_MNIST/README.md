# Deep Learning - Fashion MNIST Image Classification
This model is a convolutional neural network that classifies images of clothing items into 10 separate categories as identified by the Fashion MNIST Dataset!

## Setup
Run in the command line:
`pip3 install tensorflow`,
`pip3 install keras`,
`pip3 install numpy`

**Also make sure to unzip fashion-mnist-train.zip into this directory!**

## Technologies Used
1. Tensorflow
2. Keras
3. Convolutional Neural Network
4. Conv2D Layers
5. Dense Layers

## Results
The model's accuracy on the validation set of clothing images is about 91.67%. There is no noticeable improvement of our model's performance after the fifth epoch so, with current settings, it may be more practical to cap our model's training at 5 epochs (to save time and computational resources).

### Current Model Settings
1. Loss function is categorical_crossentropy
2. Optimization function is "Adam." See Reference [2].
3. Measuring for accuracy
4. 20 Epochs (Iterations over our dataset)
5. Batch size = 100 (this is important since we don't have to load whole datasets into memory when we use batches)
6. 20% of data taken for validation set

### Convolutional Neural Network Structure by Layer
Conv2D Layer, 8 nodes, 3 by 3 sized filter, Relu activation function
Conv2D Layer, 24 nodes, 3 by 3 sized filter, Relu activation function
Conv2D Layer, 48 nodes, 3 by 3 sized filter, Relu activation function
Flatten layer
Dense layer, 100 nodes, Relu-activated
Prediction layer: Dense layer, 10 nodes (1 for each class of clothing item), Softmax activation (to convert numerical predictions into percentages)

__Note:__I added double the amount of nodes per hidden, Conv2D layer in order to capture hierarchical features in the images.

### Model Performance per Epoch
Epoch 1/20
48000/48000 [==============================] - 58s 1ms/sample - loss: 0.4561 - acc: 0.8356 - val_loss: 0.3404 - val_acc: 0.8741
Epoch 2/20
48000/48000 [==============================] - 59s 1ms/sample - loss: 0.2905 - acc: 0.8942 - val_loss: 0.3002 - val_acc: 0.8895
Epoch 3/20
48000/48000 [==============================] - 60s 1ms/sample - loss: 0.2272 - acc: 0.9156 - val_loss: 0.2836 - val_acc: 0.8984
Epoch 4/20
48000/48000 [==============================] - 64s 1ms/sample - loss: 0.1836 - acc: 0.9327 - val_loss: 0.2564 - val_acc: 0.9103
Epoch 5/20
48000/48000 [==============================] - 61s 1ms/sample - loss: 0.1417 - acc: 0.9478 - val_loss: 0.2521 - val_acc: 0.9167
Epoch 6/20
48000/48000 [==============================] - 65s 1ms/sample - loss: 0.1051 - acc: 0.9615 - val_loss: 0.2755 - val_acc: 0.9128
Epoch 7/20
48000/48000 [==============================] - 60s 1ms/sample - loss: 0.0760 - acc: 0.9722 - val_loss: 0.3179 - val_acc: 0.9107
Epoch 8/20
48000/48000 [==============================] - 61s 1ms/sample - loss: 0.0561 - acc: 0.9797 - val_loss: 0.3354 - val_acc: 0.9082
Epoch 9/20
48000/48000 [==============================] - 60s 1ms/sample - loss: 0.0409 - acc: 0.9856 - val_loss: 0.4048 - val_acc: 0.9089
Epoch 10/20
48000/48000 [==============================] - 59s 1ms/sample - loss: 0.0289 - acc: 0.9904 - val_loss: 0.4347 - val_acc: 0.9103
Epoch 11/20
48000/48000 [==============================] - 60s 1ms/sample - loss: 0.0284 - acc: 0.9903 - val_loss: 0.4458 - val_acc: 0.9093
Epoch 12/20
48000/48000 [==============================] - 60s 1ms/sample - loss: 0.0206 - acc: 0.9933 - val_loss: 0.4839 - val_acc: 0.9079
Epoch 13/20
48000/48000 [==============================] - 59s 1ms/sample - loss: 0.0206 - acc: 0.9929 - val_loss: 0.4919 - val_acc: 0.9120
Epoch 14/20
48000/48000 [==============================] - 59s 1ms/sample - loss: 0.0203 - acc: 0.9932 - val_loss: 0.5243 - val_acc: 0.9095
Epoch 15/20
48000/48000 [==============================] - 59s 1ms/sample - loss: 0.0122 - acc: 0.9962 - val_loss: 0.5425 - val_acc: 0.9096
Epoch 16/20
48000/48000 [==============================] - 59s 1ms/sample - loss: 0.0139 - acc: 0.9952 - val_loss: 0.5722 - val_acc: 0.9072
Epoch 17/20
48000/48000 [==============================] - 59s 1ms/sample - loss: 0.0125 - acc: 0.9955 - val_loss: 0.5903 - val_acc: 0.9062
Epoch 18/20
48000/48000 [==============================] - 60s 1ms/sample - loss: 0.0122 - acc: 0.9962 - val_loss: 0.6208 - val_acc: 0.9045
Epoch 19/20
48000/48000 [==============================] - 59s 1ms/sample - loss: 0.0138 - acc: 0.9954 - val_loss: 0.6101 - val_acc: 0.9129
Epoch 20/20
48000/48000 [==============================] - 59s 1ms/sample - loss: 0.0124 - acc: 0.9959 - val_loss: 0.6125 - val_acc: 0.9082


## References
[1] https://keras.io/models/sequential/
[2] https://machinelearningmastery.com/adam-optimization-algorithm-for-deep-learning/
[3] https://keras.io/utils/
[4] https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv2D
[5] https://www.kaggle.com/dansbecker/rectified-linear-units-relu-in-deep-learning
[6] https://www.saama.com/blog/different-kinds-convolutional-filters/
[7] https://stats.stackexchange.com/questions/153531/what-is-batch-size-in-neural-network
[8] https://machinelearningmastery.com/difference-between-a-batch-and-an-epoch/


