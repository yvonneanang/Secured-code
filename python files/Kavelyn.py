from termcolor import colored
print colored("Hi, Welcome To My Calculator", "yellow") 
#i made it like that so as to print welcome to my calculator in colour yellow

num1 = input("enter first value") 
#I made it like that so as to put the value entered by the user into num1. The input function will display enter first value and then the user will enter his or her value.
num2 = input("enter second value") 
#it will let the user input his or her second value and place it in the variable num2

def addTwoNumbers(a, b): 
	#i have chosen two numbers, a and b and i have decided to add them.
	c = a + b
	#I have put a plus b in the variable c
	print "Your answer is.."
	print c
	#the answer will be displayed 
def subtractTwoNumbers(a, b):
	#i have chosen two numbers a and b and I have decided to subtract them. 
	c = a - b
	#I have subtracted the two variables and placed the result in the variable c.
	print "Your answer is.."
	print c
	#the answer will be displayed
def multiplyTwoNumbers(a, b):
	#I have chosen two numbers a and b and I have decided to multiply them.
	c = a * b
	#I have mulitipled both of them and placed the result in the variable c.
	print "Your answer is.."
	print c
	#the answer will be displayed

def divideTwoNumbers(a, b):
	#I have chosen two numbers a and b and I have decided to divide them.
	c = a / b
	#I have divided both of them and put the result in the variable c.
	print "Your answer is.."
	print c
	#the answer will be displayed
	
def moduloOfTwoNumbers(a, b):
	#I have chosen two numbers a and b and I have decided to find the modulo of both of them. 
	c = a % b
	#I have found the modulo of both of them and I have put the result in the variable c.
	print "Your answer is.."
	print c
	#the answer will be displayed

print ("What do you want to do?") #I have asked the user what he or she wants to do with his or her input above.
print "enter 1 to add the two numbers"
print "enter 2 to subtract the two numbers"
print "enter 3 to multiply the two numbers"
print "enter 4 to divide the two numbers"
print "enter 5 to find the modulo of the two numbers"
# When the user enters, 1, 2, 3, 4, or 5 the task will be carried out on the two numbers inputed at the beginning

operation = input()

if (operation == 1):
	addTwoNumbers(num1, num2)
	
elif (operation == 2):
	subtractTwoNumbers(num1, num2)
elif (operation == 3):
	multiplyTwoNumbers(num1, num2)
elif (operation == 4):
	divideTwoNumbers(num1, num2)
else:
	moduloOfTwoNumbers(num1,num2)
	
#from line 58 to line 68, the code there means that if the the user enters either 1, 2, 3, 4, or 5, the wanted operation will be carried out.