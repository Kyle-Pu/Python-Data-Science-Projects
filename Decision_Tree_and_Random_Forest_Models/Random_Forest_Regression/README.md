# Random Forest Regression Machine Learning Model for FIFA Audience Stats
A simple Random Forest Regression machine learning model for country's share of global world cup TV Audience by percentage.

## Results
This random forest regression model produces a mean absolute error (see below for definition) of about 0.2834099981618307%!

# Background and How It Works
## Random Forest Regression
A techniqe using multiple decision trees and bootstrap aggregation (or bagging). The overall idea of a random forest model is to take away the limitations of solely relying on a single decision tree. With random forest models, we're able to train multiple decision trees on different data and use averages to improve the prediction accuracy.

Random forest models are great for helping to reduce overfitting and, because they use more than one single decision tree, result in better predictive capabilities as evidenced by the lower mean absolute error (0.283 vs. 0.31 from the decision tree model)!

## Mean Absolute Error
This model's MAE based on current settings is about 0.283%!

## References
* https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html
* https://medium.com/datadriveninvestor/random-forest-regression-9871bc9a25eb
