from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Function to compare model accuracies using mean absolute error and a random forest model
def compareModels(trainX, validationX, trainY, validationY):
    model = RandomForestRegressor(random_state = 1)
    model.fit(trainX, trainY)  # Fit to training data

    predictions = model.predict(validationX)  # Use model to predict on new data
    return mean_absolute_error(predictions, validationY)

