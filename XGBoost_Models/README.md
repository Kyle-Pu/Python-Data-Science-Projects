# XGBoost Models
Here, I create a model similar to [the FIFA World Cup audience models](https://github.com/Kyle-Pu/Python-Data-Science-Projects/tree/master/Decision_Tree_and_Random_Forest_Models) but now with an **__XGBoost Model__**.

# What It Is and How It Works
XGBoost Modeling is a gradient-boosting, ensemble method. XGBoost models run with cycles, each of which contributes to the overall accuracy of our predictions. These models begin with a single model which we can find predictions with. These predictions are used to calculate a loss function which we can use to fit another model (which is added to our ensemble). Each new model we add to the ensemble minimizes our loss/cost function by using gradient descent (a minimization technique), which calculates a set of parameters for each new model to use.

## Results
The mean absolute error of the current model and parameters is 0.25249035383264223.

The current parameter settings are:
1. n_estimators = 1000
2. early_stopping_rounds = 5
3. learning_rate = 0.05

n_estimators controls how many times we want to go through the XGBoost modeling cycle (also equal to the number of models in our ensemble). The higher this setting, the more likely it is that our model is overfitting. We can, however, control overfitting with early_stopping_rounds which controls how many consecutive models can show either no or negative growth in the accuracy of our model before stopping the modeling process (the cycle breaks when n_estimator models have been created or when the number of early stopping rounds we specify is reached). The learning_rate of our model allows us to penalize models as we create more and more, therefore further limiting the overfitting effects of adding too many models into our ensemble. 

An optional parameter we could implement in our model is n_jobs, which is usually set to the number of CPU cores of the computer). This creates parallel jobs, but really is only necessary when we have gigantic datasets that will take an impracticable amount of time to train.

## Set Up
Just make sure you have these three libraries installed:
1. XGBoost: `pip3 install xgboost`
2. pandas: `pip3 install pandas`
3. scikit-learn: `pip3 install sklearn`

## [Reference](https://github.com/fivethirtyeight/data/tree/master/fifa) For Data and Description Below
This directory contains the data behind the story [How To Break FIFA](http://fivethirtyeight.com/features/how-to-break-fifa/).

The data file `fifa_countries_audience.csv` includes the following variables:

Header | Definition
---|---------
`country` | FIFA member country
`confederation` | Confederation to which country belongs
`population_share` | Country's share of global population (percentage)
`tv_audience_share` | Country's share of global world cup TV Audience (percentage)
`gdp_weighted_share` | Country's GDP-weighted audience share (percentage)

