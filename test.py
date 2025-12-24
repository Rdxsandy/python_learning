import math

def triangle(a, b, c):
    return a + b + c

def rectangle(a, b, c, d):
    return a + b + c + d

def circle(r):
    return 2 * math.pi * r


shape = input("Enter shape (circle / rectangle / triangle): ")

if shape == "circle":
    r = int(input("Enter radius: "))
    print(circle(r))

elif shape == "rectangle":
    a = int(input("Enter side 1: "))
    b = int(input("Enter side 2: "))
    c = int(input("Enter side 3: "))
    d = int(input("Enter side 4: "))
    print(rectangle(a, b, c, d))

elif shape == "triangle":
    a = int(input("Enter side 1: "))
    b = int(input("Enter side 2: "))
    c = int(input("Enter side 3: "))
    print(triangle(a, b, c))

else:
    print("Invalid shape")
