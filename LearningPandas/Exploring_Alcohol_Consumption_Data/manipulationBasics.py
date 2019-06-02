print("Loading modules and data...")
import pandas as pd

# Import the data from csv format
drinks = pd.read_csv("drinks.csv")

# Some summary information
print("\n\nHere's a look at some entries from the original dataset:\n")
print(drinks.head())

print("\n\nA quick overview of our data:\n")
print(drinks.describe())



# WIP!!!!!
