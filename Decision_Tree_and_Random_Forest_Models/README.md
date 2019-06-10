# Decision Tree Vs. Random Forest Regression Machine Learning Models for FIFA Audience Stats
In this repo, I explore the differences between decision tree regression ML models and random forest regression ML models! The dataset contains information about worldfide FIFA TV viewing audiences and our models' goal is to predict the `tv_audience_share` of each country!

## Mean Absolute Error (MAE)
This is a simple metric to measure the performance of our model. With mean absolute error, we find the average, positive difference between each element's model-predicted value and the actual value. This scheme means that every element's accuracy has equal weight in the final error value.

Each model's MAE will be in the appropriate directory's README.md

## Reproducibility
I used the `random_state` parameter when creating the models so everyone running this program will get the same results. `random_state` ensures that our data breakup (from all the data into training and cross validation segments) is the same no matter when the program is run.

## Setup
Make sure to have scikit-learn and Pandas installed before attempting to run our program!

Simply run `pip3 install sklearn` as well as `pip3 install pandas` to get the necessary modules on your device!

## [Reference (The Dataset and Description Below Are Not My Property)](https://github.com/fivethirtyeight/data/tree/master/fifa)
This directory contains the data behind the story [How To Break FIFA](http://fivethirtyeight.com/features/how-to-break-fifa/).

The data file `fifa_countries_audience.csv` includes the following variables:

Header | Definition
---|---------
`country` | FIFA member country
`confederation` | Confederation to which country belongs
`population_share` | Country's share of global population (percentage)
`tv_audience_share` | Country's share of global world cup TV Audience (percentage)
`gdp_weighted_share` | Country's GDP-weighted audience share (percentage)
