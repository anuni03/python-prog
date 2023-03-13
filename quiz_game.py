print("Welcome to my computer quiz!")
playing= input("Do you want to play?  ")
print(playing)
count=0

if playing.lower() != "yes":
    quit()


print("Okay! Let's play :)")

answer=input(" Q1 What does CPU stands for? ").lower()
if answer == "central processing unit":
    print("Correct!")
    count+=1
else:
    print("Incorrect!")


answer=input(" Q2 What does GPU stands for? ").lower()
if answer == "graphics processing unit":
    print("Correct!")
    count+=1
else:
    print("Incorrect!")


answer=input(" Q3 What does RAM stands for? ").lower()
if answer == "random access memory":
    print("Correct!")
    count+=1
else:
    print("Incorrect!")



answer=input(" Q4 What does ROM stands for? ").lower()
if answer == "read only memory":
    print("Correct!")
    count+=1
else:
    print("Incorrect!")


answer=input(" Q5 What does PSU stands for? ").lower()
if answer == "power supply unit":
    print("Correct!")
    count+=1
else:
    print("Incorrect!")


print("You got "+str(count)+" questions correct")
print("You got "+str((count / 5)*100)+"%")
