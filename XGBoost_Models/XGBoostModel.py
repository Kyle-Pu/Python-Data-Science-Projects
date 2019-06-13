print("Loading modules and data...\n")
import pandas as pd
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# Error Handling (Please comment the below two lines out when editing the program. It's usually not a good idea to ignore all warnings!!!)
import warnings
warnings.filterwarnings('ignore')

# Prep our data
fifaData = pd.read_csv("fifa_countries_audience.csv")
y = fifaData['tv_audience_share']  # These are our labels
fifaData.drop(["country", "confederation", "tv_audience_share"], axis = 1, inplace = True)  # We drop categorical data (country, confederation) and the data we want to predict (tv_audience_share)
print("Let's take a look at our data:\n", fifaData.head(), "\n")

trainX, validateX, trainY, validateY = train_test_split(fifaData, y, random_state = 1)

# Create our gradient boost model
numEstimators = 1000
stoppingRounds = 5
rate = 0.05
model = XGBRegressor(random_state = 0, n_estimators = numEstimators, early_stopping_rounds = stoppingRounds, learning_rate = rate)  # Set a random_state for reproducibility and high n_estimators for higher accuracy with an early_stopping_rounds of 5 to avoid overfitting

# Fit the model and use it to predict on new data
model.fit(trainX, trainY)
predictions = model.predict(validateX)
mae = mean_absolute_error(predictions, validateY)

print("\n--->The model's accuracy with n_estimators = ", numEstimators, " and early_stopping_rounds = ", stoppingRounds, " yields a mean absolute error of ", mae, "!", sep = "")

