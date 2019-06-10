# Modeling With Imperfect Data
Here, I explore creating machine learning models with __*missing data*__!

## Handling Missing Data
We have a few different options for handling missing data:
  1. Dropping columns with missing data
  2. Using __**imputation**__ to fill in missing values with related data such as the mean, median, or mode of the numbers in the column or a specified constant.
  3. Using imputation as well as creating columns to denote whether or not the original data had a missing value in each row (True or False).

## Handling Categorical Data
We can't directly plug in categorical data (strings/text) into our models so we have a few different options to process such data including
  1. Dropping columns with missing data
