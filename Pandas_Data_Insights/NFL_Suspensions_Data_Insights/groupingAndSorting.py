print("Loading modules and data...")
import pandas as pd
suspensions = pd.read_csv("nfl-suspensions-data.csv")

# Some summary information
print("\n\nHere's a look at some entries from the original dataset:\n")
print(suspensions.head())

print("\n\nA quick overview of our data:\n")
print(suspensions.describe())


# Grouping Functions
print("\n\nHow many suspensions each team has:")
team_suspensions = suspensions.groupby("team").size()     # groupby is a really neat function that groups our data by common attributes!
print(team_suspensions)

print("\n\nTeams sorted by most suspensions to least suspensions:")
teamSuspense = suspensions.groupby("team").team.count().sort_values(ascending = False)
print(teamSuspense)

print("\n\nYears sorted by most suspensions to least suspensions:")
offenses = suspensions.groupby("year").size().sort_values(ascending = False)
print(offenses)


# CURRENTLY BUGGY (CHECK GITHUB ISSUE PLEASE)!!!
print("\n\nLongest and shortest suspensions of a member on each team:")
longSuspense = suspensions.groupby(['team']).games.agg([min, max])
print(longSuspense)


# Multi-Indexing
print("\n\nMulti-Indexed grouping by team AND player to see detailed information about each team, its players, and its player's number of suspensions:")
multiSuspense = suspensions.groupby(['team', 'name']).name.count()
print(multiSuspense)

