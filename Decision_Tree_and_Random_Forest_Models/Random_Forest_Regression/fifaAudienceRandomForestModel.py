print("Loading modules and data...")
import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
filePath = "../fifa_countries_audience.csv"
fifaData = pd.read_csv(filePath)      # Reading in our data!
print("\nAll data has been loaded!")

# Setting Up the Model
print("\n\nPreparing the model...")
y = fifaData.tv_audience_share   # Store the values we want to predict in y (convential predictions label)
features = ["population_share", "gdp_weighted_share"]
X = fifaData[features]    # Store all the features data in X (conventional features label)

# Split our data
train_X, validation_X, train_y, validation_y = train_test_split(X, y, random_state = 1)

print("\nTraining model...")
model = RandomForestRegressor(random_state = 1)
model.fit(train_X, train_y)

print("\n\nModel is trained! Now predicting on new data...")
validation_predictions = model.predict(validation_X)
mae = mean_absolute_error(validation_predictions, validation_y)

print("\nAll processing has completed. The mean absolute error of our model's prediction is: {}".format(mae))

# Compare the mean absolute error to the magnitude of our data
avgVal = fifaData.tv_audience_share.mean()
print("\nThis model's mean absolute error is approximately {}% of the average value of TV audience shares ({})".format(round(mae / avgVal, 5), round( avgVal, 5)))
print("This means that for each prediction, the model is about {} units off of the actual value!".format(round(mae, 3)))
