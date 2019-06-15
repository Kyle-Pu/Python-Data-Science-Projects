import numpy as np
from sklearn.model_selection import train_test_split

from tensorflow.python import keras
from keras.utils import to_categorical
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense, Flatten, Conv2D

# PREPROCESSING
imgSquareSize = 28  # Pictures are 28 * 28 pictues (low resolution)
numLabels = 10 # There are 10 different types of clothing pictured in our images!

def prepData(data):
    processedY = to_categorical(data[:, 0], numLabels) # One-hot encode labels for categorical_crossentropy loss function. Labels are stored in the first column of our data.

    X = data[:, 1:] # Use all rows and columns except for the first column as our image data
    numImages = data.shape[0] # Number of rows
    processedX = X.reshape(numImages, imgSquareSize, imgSquareSize, 1)
    processedX = processedX / 255 # Restrict pixel intensity range to 0 - 1
    
    return processedX, processedY

print("\nLoading and preprocessing data...")
data = np.loadtxt("fashion-mnist_train.csv", skiprows = 1, delimiter = ',')
X, y = prepData(data)

# MODELING
print("\nConstructing convolutional neural network...")
convolutionalNN = Sequential()

# Conv2D Layers (each new layer has 2 times the number of filters/kernels in order to help learn hierarchical features)
convolutionalNN.add(Conv2D(8, kernel_size = 3, activation = 'relu', input_shape = (imgSquareSize, imgSquareSize, 1)))
convolutionalNN.add(Conv2D(24, kernel_size = 3, activation = 'relu'))
convolutionalNN.add(Conv2D(48, kernel_size = 3, activation = 'relu'))

convolutionalNN.add(Flatten())
convolutionalNN.add(Dense(100, activation = 'relu'))

# Prediction layer
convolutionalNN.add(Dense(numLabels, activation = 'softmax')) # The softmax function will turn our numerical predictions into probabilities

print("\nCompiling and fitting the convolutional neural network...")
convolutionalNN.compile(loss = "categorical_crossentropy", optimizer = 'adam', metrics = ['accuracy']) # Model compilation
convolutionalNN.fit(X, y, batch_size = 100, epochs = 20, validation_split = 0.2) # 20 epochs = 20 iterations over the dataset!


