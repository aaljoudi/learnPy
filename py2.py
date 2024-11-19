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