import random



top_of_range=input("Type a number: ")

if top_of_range.isdigit():
    top_of_range=int(top_of_range)
    if top_of_range<=0:
          print("Please enter a number greater than zero next time")
          quit()
else:
    print("Please enter a number next time")
    quit()
    
r=random.randrange(0,top_of_range)
guesses=0
while True:
    guesses+=1
    user_guess=input("Make a guess: ")
    if user_guess.isdigit():
        user_guess=int(user_guess)
        if user_guess<=0:
          print("Please enter a number greater than zero next time")
          quit()
    else:
     print("Please enter a number next time")
     continue

    if user_guess==r:
      print("You got it right!")
      break
    
    elif user_guess > r:
            print("You are above the number")
    else:
            print("You are below the number")

print("You got it in", guesses ,"guesses")
