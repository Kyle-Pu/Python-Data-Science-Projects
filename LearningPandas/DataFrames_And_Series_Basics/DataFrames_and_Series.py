import pandas as pd
# from lists.py import modList

restaurantOrders = pd.DataFrame({"Kyrie": ["Beef Jerkey", "Bologna"], "Tayvon": ["Fried Chicken", "Turkey"]}, index = ["Order 1", "Order 2"])

print("DataFrame:")
print(restaurantOrders)


items = ["Bread", "Bagels", "Cereal", "Milk", "Sugar", "Flour"]
labels = ["Item " + str(num) for num in range(1, len(items) + 1)]
shoppingList = pd.Series(items, index = labels, name = "Shopping List!")

print("\nSeries:")
print(shoppingList)

'''
shoppingList = []
keepGoing = True

while(keepGoing):
    modList(shoppingList)
    toGo = input("Press q to quit, any other key to continue\n")

    if(toGo.upper() == "Q"):
        keepGoing = False

labels = ["Item " + str(num) for num in range(1, len(items) + 1)]
shoppingSeries = pd.Series(shoppingList, index = labels, name = "Shopping Series!")
'''


#Give user option to save the DataFrame and Series to a CSV or Excel file
opt = input("\n\nWould you like to save this data onto your computer in a CSV doc? Enter 'Y' for Yes, anything else for No: ")
if opt.upper() == 'Y':
    restaurantOrders.to_csv("orders.csv")
    shoppingList.to_csv("shoppingSeries.csv")

opt = input("\nWould you like to save this data onto your computer in an Excel spreadsheet? Enter 'Y' for Yes, anything else for No: ")
if opt.upper() == 'Y':
    restaurantOrders.to_excel("orders.xlsx", sheet_name = "All Orders")
    shoppingList.to_excel("shoppingList.xlsx", sheet_name = "Shopping List")
