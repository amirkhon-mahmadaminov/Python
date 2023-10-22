import time
while True:
    try:
        d = float(input("Enter the diameter: "))
    except ValueError:
        print("Please Enter A Valid Number")
    else:
        if d == 0:
            print ("Quitting...")
            time.sleep(1)
            break;
        else:
            pi = 3.14
            c = pi * d
            print("Circumference is: " + str(c))
