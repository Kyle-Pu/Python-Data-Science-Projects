import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

data = pd.read_csv("drug-use-by-age.csv")
data.replace("-", np.NaN, inplace = True)

y = data["alcohol-frequency"]
X = data.drop(['alcohol-frequency'], axis = 1)
# X = data.select_dtypes(exclude = ["object"])  Note: THIS DELETES COLUMNS WITH NaN VAULES SINCE NaN IS OF OBJECT TYPE!!! (I was stuck for half an hour trying to find out why all columns with missing values were being dropped haha)

trainX, validateX, trainY, validateY = train_test_split(X, y, random_state = 1)

colsWithMissing = [col for col in X.columns if X[col].isnull().any()]
print("Columns with missing data:", colsWithMissing)

trainX.drop(colsWithMissing, axis = 1)


data.replace("-", np.NaN, inplace = True)  # Replace all dashes in data with NaN. inplace = True because we don't need to retain the original dataset! Note: inplace = False by default which means it doesn't alter the original data (it assigns your result to a new variable).




