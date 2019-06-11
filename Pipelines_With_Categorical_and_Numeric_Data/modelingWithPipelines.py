print("Loading modules and data...\n")
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder

# Prep our data
fifaData = pd.read_csv("fifa_countries_audience.csv")
y = fifaData['tv_audience_share']
fifaData.drop(["country", "tv_audience_share"], axis = 1, inplace = True)
print("Let's take a look at our data:\n", fifaData.head())

trainX, validationX, trainY, validationY = train_test_split(fifaData, y, random_state = 1)

numericalColumns = [col for col in fifaData.columns if fifaData[col].dtype in ['int64', 'float64']]
categoricalColumns = [col for col in fifaData.columns if fifaData[col].dtype == 'object']

# Preprocessing algorithms
processNumerical = SimpleImputer(strategy = 'mean')
processCategorical = Pipeline(steps = [('impute', SimpleImputer(strategy = "most_frequent")), ('onehot', OneHotEncoder(handle_unknown = 'ignore'))])
preprocessor = ColumnTransformer(transformers = [('num', processNumerical, numericalColumns), ('cat', processCategorical, categoricalColumns)])

# Define the model
model = RandomForestRegressor(n_estimators = 100, random_state = 1)

# Bundle preprocessing with modeling in a pipeline
mainPipeline = Pipeline(steps = [('preprocessor', preprocessor), ('model', model)])

# Train and fit the model
mainPipeline.fit(trainX, trainY)

# Preprocess AND predict on validation data (our pipeline allows us to streamline this process)!
predictions = mainPipeline.predict(validationX)

# Evaluate the accuracy of our model!
mae = mean_absolute_error(predictions, validationY)
print("\n--->The mean absolute error of our model is:", mae)

