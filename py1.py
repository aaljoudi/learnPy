print ("Hello world")

# Python syntax

x = 3

if x > 2:
    print ("Greater!")
    print ('That is all')

# Excersize to translate c++ code to python

x = 3

if x > 2:
    print ("Greater")
    if x == 3:
        print ("Equal")
    else:
        print ("Not equal")
else:
    print ("less")

# J-Droid excersizes - task 1

"""
Task 1:

Translate the following C++ code to Python
int x = 3;
int y = 4;

if (x > y && !(x < y)) {
  cout << "Equal";
} else if (x > 100) {
  cout << "Big";
}

"""

# Task 1 - your solution here

x = 3
y = 4

if x > y and not x < y:
    print ("Equal")
elif x > 100:
    print ("Big")

# User input

#This print function prevents the code from going to newline before input
## Note: You do not need to add a space, the comma adds a space
print ("Type a string:", end="")
s = input()
print(s)

# Printing basics

x = 3
y = 4
z = 5.6789

print (x, y)
print ("x is:", x)

# The f command means you can use {} to evaluate as an expression
print (f"x is: {x}")

# {z:.2f} format z to a float number rounded to 2 decimal places
print (f"z is: {z:.2f}")

# end="" means no new line after printing
print (x, y, end="")