# Chapter3 Practice Projects

import sys

# collatz behavior
def collatz(number):

    if (number % 2 == 0):
        result = number // 2
        print(result)
        return result
    
    else:
        result = 3 * number + 1
        print(result)
        return result

user_input = input("input: \n")
user_input = int (user_input)   # convert to int

number = collatz(user_input)    # initial value

while True: # infinite loop

    if number == 1:
        sys.exit()  # exit program when the value becomes 1
    
    else:
        number = collatz(number)    # number is in a global scope - update initial value