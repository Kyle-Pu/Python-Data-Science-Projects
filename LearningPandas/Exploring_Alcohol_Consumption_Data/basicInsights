print("Loading modules and data...")
import pandas as pd

# Import the data from csv format
drinks = pd.read_csv("drinks.csv")

# Some summary information
print("\n\nHere's a look at some entries from the original dataset:\n")
print(drinks.head())

print("\n\nA quick overview of our data:\n")
print(drinks.describe())

print("\n\nRemeaning the beer_servings data to 0 (a common processing step before working with machine learning algorithms):\n")
beerMean = drinks.beer_servings.mean()
print("Mean before mapping: " + str(beerMean) + "\n\nData meaned to 0:")
print(drinks.beer_servings.map(lambda x: x - beerMean))    # Anonymous function that subtracts the original mean from each value in the beer_servings column

# print(drinks.beer_servings)    Note: Didn't show the mapped values because .map doesn't actually modify the original data. It returns a new set.
