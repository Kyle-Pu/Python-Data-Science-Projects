def funcInFunc(func, num = 519):
    """Call a function on a number through this function! Default num value is 4    20 if nothing else is supplied!
    
    Background: Functions can call other functions within them. You can also pas    s in a function as a parameter of another function as well as set parameters    with default values!!!"""
    
    return func(num)

#Take in the number to round
num = input("What decimal number do you want to round?!??!?!!?!?? ")

#Round the number by passing in the round function to funcInFunc. If the input is invalid, catch the error
try:
    print(funcInFunc(round, float(num)))
except ValueError: 
    print("Haha. You won't break me. Input a valid float value!!!")

