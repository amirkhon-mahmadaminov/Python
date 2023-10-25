import time

def circle():
    while True:
        key = input("What do you want to find? \n1. Diameter\n2. Area\n3. Radius \n0. Menu \nOption: ")
        if key == '1':
            r = float(input("Enter Radius: "))
            d = 2 * r
            print("The diameter is: " + str(d))
        elif key == '2':
            pi = 3.14
            r = float(input("Enter radius: "))
            s = pi * r * r
            print("The result is: " + str(s))
        elif key == '3':
            d = float(input("Enter diameter: "))
            r = d / 2
            print("The result is: " + str(r))
        elif key == '0':
            break
        else:
            print("Invalid input!")

def rectangle():
    while True:
        key = input("What do you want to find? \n1. Length\n2. Breadth\n3. Area\n0. Menu \nOption: ")
        if key == '1':
            a = float(input("Enter area: "))
            b = float(input("Enter breadth: "))
            l = a / b
            print("The length is: " + str(l))
        elif key == '2':
            a = float(input("Enter area: "))
            l = float(input("Enter length: "))
            b = a / l
            print("The breadth is: " + str(b))
        elif key == '3':
            l = float(input("Enter length: "))
            b = float(input("Enter breadth: "))
            a = l * b
            print("The area is: " + str(a))
        elif key == '0':
            break
        else:
            print("Invalid input!")

def homepage():
    while True:
        print("***Main Menu***")
        print("Choose shape: ")
        print("1. Circle")
        print("2. Rectangle")
        key = input("Option: ")

        if key == '1':
            circle()
        elif key == '2':
            rectangle()
        else:
            print("Invalid input!")

print("Loading...")
time.sleep(3)
homepage()
