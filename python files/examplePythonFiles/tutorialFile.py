

#numberOfGuesses = 0
#while numberOfGuesses < 3: #this is called a loop
#    secretWord = raw_input("Hi, please the password: >>> ")
#    if secretWord == "banku":
#        print "Welcome to the secret society of banku..."
#        break # Exits the loop
#    else:
#        print "Sorry, please try again."
#    numberOfGuesses = numberOfGuesses + 1
#    
#
#
#
#print "Hi, " + usersName + "! Nice to meet you!"
#
#usersName = raw_input("Hi, please enter your name")
#
#nameNumber = input("How many times should I print your name?")
#
#print ((usersName + " ") * nameNumber)
#
#usersName = raw_input("Hi, please enter your name: >>> ")
#if usersName == "Phil":
#    print "Phil is the absolute coolest!!!!"
#else:
#    print "Hey " + usersName + ". Great to meet you."

#from Tkinter import *
#master = Tk()
#PassWord= Entry(master, bd = 5, width = 20, show ="*")
#PassWord.pack()
#master.mainloop()

import getpass
name=getpass.getpass("What is your name?:>>>")
print len(name)
print name[0:5]

