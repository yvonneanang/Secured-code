while 1==1:
    score = input ("Enter your score")
    if score <=100 and score>=80:
        grade= "A"
       
    elif score <=79 and score>=70:
        grade+= "B"
        
    elif score <=69 and score>=60:
        grade+= "C"
        
    elif score <=59 and score>=50:
        grade+= "D"
        
    elif score <=49 and score>=45:
        grade+= "E"
        
    else:
        grade+= "F"
        
        
    print "Do you want to continue?"
    print "Type 'yes' to continue  "
    print "Type 'no' to stop  "
    continueGrading = raw_input("Enter word of choice")
    if continueGrading == "no":
        break
print "Your grades were..."
print grade

    
    
    


    