from termcolor import colored
print colored("Welcome To The WASSCE Grading System","blue")
print "This application tells you your grade for any mark or score you input."
print "Get ready to rumble!!!!"

marks = input("what is your score?")

if (marks <= 100 and marks >= 80):
	print "Hurray and congratulations!!!,  you had an A"

elif (marks <=79 and marks >= 75):
	print "Good job, you had a B"

elif (marks <=74 and marks >=70):
	  print "Quite fair, you had a C"

elif (marks <=69 and marks >= 65):
	print "Fair enough,  you had a D"

elif (marks <=59 and marks >= 50):
	  print "You can do better, you had an E"
else:
	  print colored("What a bad performance!!!\n Better luck next time.\n Hehehe :-D\n...Oh and by the way, just so you know...you had A BIG FAT F. Hahaha...\nDon't mind me erh..Just don't stop trying okay?", "red")

print colored("THANK YOU FOR USING WASSCE GRADING SYSTEM!!! Bye!!!", "yellow" )

