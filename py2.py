print("Hello world")

# Functions

def add(x, y):
    return x + y

# J-Doodle excersize
## This function does not work as intended
def poly(x, coef):
    sum = 0
    for y in coef:
        i = 0
        sum += coef[i] * x**i
        i += 1
    
    return sum

coeffs = [4, 3, 1, 5]
print (poly(2, coeffs))

# Returning two things from a function

def f3(n):
    return n+10, n-10

c, d = f3(5)
print(c, d)

# Function with default parameters
def f4 (i = 10, j = 5):
    return i - j

## all calls below are valid
w = f4()
w2 = f4(3)
w3 = f4(3, 5)
w4 = f4(j = 2, i = 5) #alters the order of parameters in the function

print (w, w2, w3, w4)

# Loops

def loop():
    r = range(0, 10, 1)
    ## range(start, upToButNotIncluding, incremenation)

    print ("r:", r)

    for item in r:
        print (item, end="")
    
    print()

print (loop())

## Char looping

def loop2():
    s = "data mining"
    for c in s:
        print (c, end="-")

    print()

print (loop2())

# Working with files

def FileRead():
    infilename = input("Enter a file name: ")

    infile = open(infilename, "r")

    lineNumber = 1

    for line in infile:
        print (str(lineNumber) + ":", line[:-1])
        lineNumber += 1
    
    infile.close()

x = FileRead()