import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

import sys # Import capability to grab a function from a file in a different directory
sys.path.insert(0, '../Tools/')
from modelComparison import compareModels

import warnings
warnings.simplefilter(action = "ignore", category = FutureWarning) # Suppress error output: python3.6/site-packages/sklearn/ensemble/forest.py:245: FutureWarning: The default value of n_estimators will change from 10 in version 0.20 to 100 in 0.22. "10 in version 0.20 to 100 in 0.22.", FutureWarning)


# Import data
drugUse = pd.read_csv("drug-use-by-age.csv")

# Taking a Look At Original Data
print("\n\nHere's a look at the original dataset!\n", drugUse.head(), sep = "\n0")

# Replace all dashes (represents missing value)  in data with NaN. inplace = True because we don't need to retain the original dataset! Note: inplace = False by default which means it doesn't alter the original data (it assigns your result to a new variable).
# We want to predict alcohol-frequency values so set all other columns as features
drugUse.replace("-", np.NaN, inplace = True)

y = drugUse["alcohol-frequency"]
X = drugUse.drop(['alcohol-frequency'], axis = 1) # axis = 1 signifies using columns

'''
X = drugUse.select_dtypes(exclude = ["object"])  

Note: THIS DELETES COLUMNS WITH NaN VAULES SINCE NaN IS OF OBJECT TYPE!!! (I was stuck for half an hour trying to find out why all columns with missing values were being dropped haha)
'''

# Find columns with missing data entries
colsWithMissing = [col for col in X.columns if X[col].isnull().any()]
print("\n\nColumns with missing data:", colsWithMissing)



# Method 1 (Dropping Columns With Missing Data Values)
# Split our data
trimmedX = X.drop(colsWithMissing, axis = 1, inplace = False)
trainX, validateX, trainY, validateY = train_test_split(trimmedX, y, random_state = 1)
print("\n\nHere's a peek at our training data when we drop all columns with missing values!", trainX.head(), sep = "\n")

methodOneMAE = compareModels(trainX, validateX, trainY, validateY)
print("\n-->Dropping all columns with missing data produces a random forest model with MAE:", methodOneMAE)



# Method 2 (Imputation)
imputer = SimpleImputer(strategy = "most_frequent")
trainX, validateX, trainY, validateY = train_test_split(X, y, random_state = 1)
imputedTrainX = pd.DataFrame(imputer.fit_transform(trainX))
imputedValidateX = pd.DataFrame(imputer.transform(validateX))

imputedTrainX.columns = trainX.columns
imputedValidateX.columns = validateX.columns

print("\n\nHere's a peek at our training data when we impute missing values!", imputedTrainX.head(), sep = "\n")

methodTwoMAE = compareModels(imputedTrainX, imputedValidateX, trainY, validateY)
print("\n-->Imputing missing values with average of column data produces a random forest model with MAE:", methodTwoMAE, "\n\n")

