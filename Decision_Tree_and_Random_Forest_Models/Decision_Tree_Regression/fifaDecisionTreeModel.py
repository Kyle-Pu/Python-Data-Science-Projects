print("Loading modules and data...")
import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
filePath = "../fifa_countries_audience.csv"

# Data Preparation
print("\nPreparing data...")
fifaData = pd.read_csv(filePath)
features = ["population_share", "gdp_weighted_share"]
X = fifaData[features]
y = fifaData.tv_audience_share
trainingData, validationData, trainingLabels, validationLabels = train_test_split(X, y, random_state = 1)

# Create and train the model
print("\nTraining model...")
model = DecisionTreeRegressor(random_state = 1)
model.fit(trainingData, trainingLabels)

# Predictions for new, validation data
print("\nUsing the model to predict new values...")
predictions = model.predict(validationData)

# Error Calculation
mae = mean_absolute_error(validationLabels, predictions)
print("The mean absolute error of this decision tree model was {}".format(mae))
print("\n\nSee the random forest regression model results in this repo!!!")
