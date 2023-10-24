import time
def menu():
    print("***Menu***")
    print("1. Find P")
    print("2. Find S")
    key = input("Option: ")

    if key == "1":
        a = float(input("Enter the height of Rectangle: "))
        b = float(input("Enter the width of Rectangle: "))
        c = float((a + b) * 2)
        print("The result is: " + str(c))

    elif key == "2":
        a = float(input("Enter the height of Rectangle: "))
        b = float(input("Enter the width of Rectangle: "))
        c = float(a * b)
        print("The result is: " + str(c))

    else:
        print ("Invalid Input!")

print ("Opening...")
time.sleep(1)
while True:
    menu()
