import time
print ("Welcome to Nasa Calculator")
a = input("Enter first number: ")
b = input("Enter second number: ")
c = input("Enter operator: ")
d = 0

a = int(a)
b = int(b)


if c == '+':
    d = a + b
elif c == '-':
    d = a - b
elif c == '*':
    d = a * b
elif c == '/':
    d = a / b
else:
    print("Fatal Error")

time.sleep(1)
print("Analyzing your inputs")
time.sleep(3)
print("....")
time.sleep(3)
print("Almost done")
time.sleep(3)
print("Idk, Use your head")
time.sleep(3)
print("r u still here \nOkay the answer is below")
time.sleep(3)
print(d)
