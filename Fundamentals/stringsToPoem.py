print("Welcome to Build-A-Narrative-Poem!")

food = input("What's one of your favorite foods? ")
reason = input("Why do you like that food so much?!? ")

friend = input("Who's one of your best friends? ")
reason2 = input("Why do you like them so much? ")

device = input("What's one of your favorite electronic devices? ")
reason3 = input("Why do you like it so much? ")

narrative = """
{} is one of my favorite foods.
I love it so much because {}
               
{} is my friend and makes me happy
I like them because {} and they cheer me up when Ms. Cornejo gives her FRAPPY

{} is one of my favorite devices
I like it so much because {}. I get so happy, it makes me wanna throw dices!""".format(food, reason, friend, reason2, device, reason3)

print(narrative)
