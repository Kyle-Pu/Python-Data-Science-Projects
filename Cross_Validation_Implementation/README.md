# Cross-Validation Implementation
Here, I create a model similar to [the FIFA World Cup audience models](https://github.com/Kyle-Pu/Python-Data-Science-Projects/tree/master/Decision_Tree_and_Random_Forest_Models) but now including cross-validation! I run cross validation over 5 folds and 10 different parameter settings for n_estimators (the number of trees in our forest) to see what setting gives the best model.

## Results
n_estimators = 150 gives the best model after running cross validation on these settings. Feel free to check out the graph below!

<p align = "center">
  <img src=graph.png>
</p>

## How It Works
Cross-validation is a better indicator of model quality because it breaks up our dataset into multiple "folds." We can use a pipeline to train our model on all data excluding each fold (this is an iterative process so we train our model on all data except for the first fold, then all data except for the second fold, etc). Each time, the fold that is excluded from the training data is treated as the validation set so we can measure our model's quality with all data.

## Why?!?
Cross-validation is useful because it addresses the randomness of only using one chunk of our data as validation data. For example, if we have a dataset with only 1000 rows and we use 200 of them for validation data, there's a chance that the model will perform well on the 200 selected while performing poorly on other data.

Cross-validation gets around this issue because it allows us to include every single data point in the validation set at some point along the modeling process. 
