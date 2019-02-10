
print(2)        # print a number
print(2.34)     # print a float
print(2 + 2)    # print addition
print(3 + 4.5)  # print addition with float
print(4 - 2)    # print subtraction
print(2 * 3)    # print multiplication
print(4 / 2)    # print division

print(3 * 4 + 5)        # combine multiplication and addition
print(3 * (4 + 5))      # print order of operations
print(10 % 3)           # print the remainder of division (1)


my_num = 5      # store numbers inside of variables
print(my_num)   # print number variable

print(str(my_num))      # you can also convert numbers into a string
print(str(my_num) + " my favortie number")


print(int(2.34))        # int function will give you the whole number

# common functions used in Python related to numbers

my_num = -5
print(abs(my_num))      # abs will give absolute value of a number -5 = 5
print(pow(3, 2))        # pow is number to the power of
print(max(3, 4))        # max will print larger number in sequence
print(min(4, 6, 93))    # min will print smaller number in sequence
print(round(3.2))       # round will round down
print(round(3.7))       # round will round up


from math import *      # this module will access extra math functions
print(floor(3.7))       # example
print(ceil(3.7))        # example
print(sqrt(36))         # example
