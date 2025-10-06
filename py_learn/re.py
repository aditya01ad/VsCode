## Python Notes ##
###-------------------------------------------------------------------
# basics
def revise() :
    x = 10
    y = 3.14
    z ="Hi"
    is_valid = True
    n = None

    print(type(n))

    # arith + - * / % ** 
    # comp ++ != <= >= < >
    # Logical and or not
    # Assign + += -+ *= 
    # Membership in ; not in

    a, b = 5, 2
    print(a**b)
    print(7//3)
    print(7%3)

    # strings

    s = "Python"
    print(s.lower())
    print(s[::-1])
    print(s[0:3])
    print("Py" in s)

    # List 
    nums = [1, 2, 3]
    nums.append(4)
    # Tuple
    point = (2,3)
    # Set
    S = {1, 2, 2, 3}
    # Dict
    person = { "name" : "Alice", "age" : 23}
    print(person["name"])


    # conditionals
    x = 5
    if x> 0 :
        print("+")
    elif x == 0 :
        print("zero")
    else :
        print("-");
        
    # Loops
    print("for loop")
    for i in range(3) :
        print(i)
        
    print("while loop")
    while x > 0 :
        print(x)
        x -= 1
        
# Functions

def welcome(name = "world") :
    return f"welcome to sbs, {name}"

# print(welcome("Adi"))
# print(revise())

### ---------------------------------------------------------------
# Exercisee

# square of even
def print_sqrs_of_even() :
    n = 15
    print("squares of even numbers")
    for i in range(n) :
        if i %  2 == 0 :
            print(f"square of {i} = " + f"{i**2}")

# create a dictionari to store "num" : "square"
squares = {num : num ++ 2 for num in range(1,11) if num % 2 == 0}
print(squares) # altr : squares = {}; squares[num] = num ** 2;

# List comprehension way
squares = [i ** 2 for i in range(1, 6)]
# evens = [i for i in range(10) if i % 2 == 0]

### -----------------------------------------------------------------

# Generator Expressions
gen = (i ** 2 for i in range(5))
print(next(gen))
print(next(gen))

# Error Handling 

try :
    x = 10 / 0
except ZeroDivisionError as e :
    print("Error : ", e)
else :
    print("No error")
finally :
    print("Always runs")

# Modules & Imports
import math as m #import math
print(m.sqrt(16))
print(m.pi)
from math import sqrt, pi
print(sqrt(pi))

#File Handling
#write
name = "Frnd"
with open("data_re.txt", "w") as f :
    f.write(welcome(name))
    
with open("data_re.txt", "r") as f :
    content = f.read()
print(content)    

## Exercise :
#1.Create a list of all numbers between 1 and 50 that are divisible 
# by both 3 and 5 (use list comprehension).
#2.Save that list into a file called multiples.txt 
# (one number per line).
#3.Then read the file back and print the numbers.