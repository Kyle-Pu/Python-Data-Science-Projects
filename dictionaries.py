#Ask for a starting phrase!
phrase = input("What string would you like to deconstruct?!?!?!? ")

#Split the string by whitespace
splitUp = phrase.split()

#Create a dictionary using dictionary comprehension
#Use the first letter of each word as the key
#Use the actual word as the value
#No periods or commas at the end of each word is allowed
dictionary = {word.strip(".,")[0]: word.strip(",.") for word in splitUp}

print(dictionary)
