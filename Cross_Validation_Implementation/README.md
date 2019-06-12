# Cross-Validation Implementation
Here, I create a model similar to []() but now including cross-validation!

## How It Works
Cross-validation is a better indicator of model quality because it breaks up our dataset into multiple "folds." We can use a pipeline to train our model on all data excluding each fold (this is an iterative process so we train our model on all data except for the first fold, then all data except for the second fold, etc). Each time, the fold that is excluded from the training data is treated as the validation set so we can measure our model's quality with all data.

## Why?!?
Cross-validation is useful because it addresses the randomness of only using one chunk of our data as validation data. For example, if we have a dataset with only 1000 rows and we use 200 of them for validation data, there's a chance that the model will perform well on the 200 selected while performing poorly on other data.

Cross-validation gets around this issue because it allows us to include every single data point in the validation set at some point along the modeling process. 
