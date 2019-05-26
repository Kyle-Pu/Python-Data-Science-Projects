def funcInFunc(func, num = 519):
    """Call a function on a number through this function! Default num value is 5    19 if nothing else is supplied!
    
    What I Learned: Functions can call other functions within them. You can also    pass in a function as a parameter of another function as well as set
    parameters with default values!!!
    
    funcInFunc(round, 50.8)
    >>>51"""
    
    return func(num)

#Take in the number to round
num = input("What decimal number do you want to round?!??!?!!?!?? ")

#Round the number by passing in the round function to funcInFunc. If the input is invalid, catch the error
try:
    print(funcInFunc(round, float(num)))
except ValueError: 
    print("Haha. You won't break me. Input a valid float value!!!")

