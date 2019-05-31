from matplotlib import pyplot as plt

print("Welcome to your Plotting Calculator!")
num = int(input("How many numbers would you like to plot? "))

yCoords = []

for i in range(num):
    yCoords.append(int(input("What number would you like to add to your plot? ")))

#Plot connected by straight line segments
plt.plot(yCoords)

plt.ylabel("Numbers In Your List")
plt.title("Your List!")
plt.show()
