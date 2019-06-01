def modList(current):
    opt = input("What would you like to do? Add to the list, remove from the list, or view the list? ")
    if(opt.upper() == "ADD"):
        toAdd = input("What would you like to add? ")
        current.append(int(toAdd))
    elif(opt.upper() == "REMOVE" or opt.upper() == "R"):
        toAdd = input("Which index would you like to remove? ")
        
        if(int(toAdd) >= 0 and int(toAdd) < len(toAdd)):
            current.pop(int(toAdd))
        else:
            print("Index out of bounds...\n")
    elif(opt.upper() == "VIEW" or opt.upper() == "V"):
        print(current)
    else:
        print("Please input a valid value!!!\n")
        modList(current)

print("Hello and welcome to Build-A-List!")

myList = []
print("List initialized... Now it's time to build your list!")

keepGoing = True

while(keepGoing):
    modList(myList)
    toGo = input("Press q to quit, any other key to continue\n")

    if(toGo.upper() == "Q"):
        keepGoing = False



