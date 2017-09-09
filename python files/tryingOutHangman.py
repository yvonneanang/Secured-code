print "Welcome to Yvonne Anang's version of Hangman!!!\nThis game was originally created by Kunal Kamath and Harish Shanker. I just copied some parts...:-D"
print"This is a guess game. Enter a word and then anyone else has to guess the word. The guesser has only five number of times to guess so...GUESS WELL. "
print "Let the game begin!!!"
import getpass
while 1 == 1:    
    guessWord=getpass.getpass("Enter a word please:>>>")
    numberOfGuesses=0
    while numberOfGuesses < 5:
        guess=raw_input("Please enter  the guess word:>>>")
        if guess==guessWord:
            print "You guessed right.\nCongratulations.\n:-)"
            break
        else:
            numberOfGuessesLeft=5
            if numberOfGuesses==0:
                print "You have this number of guesses left:", numberOfGuessesLeft - 1
            if numberOfGuesses==1:
                print "You have this number of guesses left:", numberOfGuessesLeft - 2
            if numberOfGuesses==2:
                print "You have this number of guesses left:", numberOfGuessesLeft - 3
            if numberOfGuesses==3:
                print "You have this number of guesses left:", numberOfGuessesLeft - 4
            if numberOfGuesses==4:
                print "You have this number of guesses left:", numberOfGuessesLeft - 5
                print "Sorry, you guessed wrong...thanks for trying. :-)"
        numberOfGuesses = numberOfGuesses + 1
    print "The word is", guessWord
    print "Do you want to play again?"
    print "If so, type yes."
    print "If not, type no."
    choice = raw_input("Do you want to continue?:>>>")
    if choice == "no":
        break


    