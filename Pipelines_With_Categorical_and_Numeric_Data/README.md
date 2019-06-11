# Pipelines With Categorical and Numeric Data
Pipelines! Pipelines make code easier to read and less prone to errors, while also providing benefits such as higher-level functions (so we don't have to get into every detail/step of the preprocessing, analyzing, and modeling process)!

Here, I again build an ML model for __FIFA World Cup Audience Stats__, the same dataset used in the [decision tree and random forest modeling directory](https://github.com/Kyle-Pu/Python-Projects/tree/master/Decision_Tree_and_Random_Forest_Models) of this repo.

## Why Pipelines???
Just take a look at the code! It's much more concise, cleaner, and easy to read. It's also a lot easier to follow in terms of understanding how the model is created at all stages (from preprocessing of data to the training of the model)!

## Results
The mean absolute error for this model is 0.2681280382750777 with current settings. This is even lower than the lowest MAE achieved by the random forest model (in the link above). This is not due to the use of pipelines, however. This is due to the fact that I made this model take into account categorical data (the FIFA confederation each country belongs to), which likely affects audience turnout for the World Cup games.

## How It Works
1) Create a numerical transformer to work with numerical data.
2) Create a categorical transformer to work with categorical data.
3) Create a preprocessor with ColumnTransformer that bundles the numerical and categorical transformer.
4) Define a model.
5) Bundle the preprocessor with the model using a pipeline.
6) Train and fit the model with the pipeline created from Step #5.
7) Use the pipeline to process and predict on validation data.
8) Evaluate the model's accuracy (I used mean absolute error).

## [Reference](https://github.com/fivethirtyeight/data/tree/master/fifa)
Once again, this is NOT my data and the description below is NOT mine.

This directory contains the data behind the story [How To Break FIFA](http://fivethirtyeight.com/features/how-to-break-fifa/).

The data file `fifa_countries_audience.csv` includes the following variables:

Header | Definition
---|---------
`country` | FIFA member country
`confederation` | Confederation to which country belongs
`population_share` | Country's share of global population (percentage)
`tv_audience_share` | Country's share of global world cup TV Audience (percentage)
`gdp_weighted_share` | Country's GDP-weighted audience share (percentage)
