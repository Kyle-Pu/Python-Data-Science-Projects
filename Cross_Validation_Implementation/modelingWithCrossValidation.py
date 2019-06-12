print("Loading modules and data...\n")
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt

# Prep our data
fifaData = pd.read_csv("fifa_countries_audience.csv")
y = fifaData['tv_audience_share']
fifaData.drop(["country", "tv_audience_share"], axis = 1, inplace = True)
print("Let's take a look at our data:\n", fifaData.head())

numericalColumns = [col for col in fifaData.columns if fifaData[col].dtype in ['int64', 'float64']]
X = fifaData[numericalColumns]

# Running cross validation with different numbers of trees in the random forest model
def modelAccuracy(numTrees):
    mainPipeline = Pipeline(steps = [('preprocessor', SimpleImputer()), ('model', RandomForestRegressor(n_estimators = numTrees, random_state = 1))])
    cValidationScores =  -1 * cross_val_score(mainPipeline, X, y, cv = 5, scoring = "neg_mean_absolute_error") # cv = 5 creates 5 folds in our data
    return cValidationScores.mean()

# Dictionary with numTrees as keys and the model's accuracy for numTrees as values
print("\nTraining models using cross validation...")
diffTrees = [n * 50 for n in range(1, 11)]
allScores = {numTrees: modelAccuracy(numTrees) for numTrees in diffTrees}

# Optimization
print('\n\n\nAfter running cross validation on all folds of our data, the lowest mean absolute error, based off of our graph, occurs at n_estimators = numTrees = 150! This setting produces a model with an average mean absolute error of', allScores[150])

# Graph allScores to find the minimum mean absolute error setting for n_estimators
plt.plot(list(allScores.keys()), list(allScores.values()))
plt.ylabel('Cross Validation MAE Average Score')
plt.xlabel('n_estimators/numTrees')
plt.show()


