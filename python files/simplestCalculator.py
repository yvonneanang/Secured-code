
print "Welcome to my calculator."
num1 = input("Enter first number")
num2 = input("Enter second number")

def addTwoNumbers(a, b):
    c = a + b
    print c
    
def multiplyTwoNumbers(a, b):
    c = a * b
    print c

def subtractTwoNumbers(a, b):
    c = a - b
    print c

def divideTwoNumbers(a, b):
    c = a / b
    print c
while 1==1:
    print "What do you want to do with the two numbers?"
    print "type 1 to add the numbers"
    print "type 2 to multiply the numbers"
    print "type 3 to subtract the numbers"
    print "type 4 to divide the numbers"
    operation = input("Enter the operation you want to carry out with the two numbers")

    if (operation == 1):
        addTwoNumbers(num1, num2)
    if (operation == 2):
        multiplyTwoNumbers(num1, num2)
    if (operation == 3):
        subtractTwoNumbers(num1, num2)
    if (operation == 4):
        divideTwoNumbers(num1, num2)
    print "Do you want to continue?"
    print "if yes, type yes"
    print "if no, type no"
    option = raw_input("type in what you want to do")

    if (option == "no"):
        break




    