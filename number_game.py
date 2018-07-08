#Guessing Game To-Do List:
#1. Limit the number of guesses
#2. Catch when someone submits a non-integer.
#3. Print "too low" or "too high" messages for bad guesses.
#4. Let people play again.

import random


def game():
  #Generate a random number between 1 and 10 
  secret_num = random.randint(1, 10)
  #We add all the guessess in to a list. Here we created a list of guesses
  guesses = []
  
  #We used while loop here what it means it will ask for an input infintely until the condition becomes true.
  #  while True:
  #We want to make sure the guess less than 5 times. Again len is a function that all len does is len tells us the lenght of an object. So what's the length of our guesses variable? Right now is      zero. String hello have a len or length of 5 because it has five letters. As soon as the guesses is more than 5 the program ends.
  while len(guesses) < 5:
  #Try to turn this thing into a number.  
    try:
  #Get a number guess from the player.
      guess = int(input("Guess a number between 1 and 10: "))
  #This except value error will work if the user types in a non- number. Then it will print out that message below.
    except ValueError:
    #If its not a number print out the message.  
      print("{} isn't a number!".format(guess))
    #Otherwise we'll do the game
    else:  
      #Compare guess to secret number
      if guess == secret_num:
        print("You got it! My number was {}".format(secret_num))
        break
        #Here give you hint if your guess number was lower the secret number.
      elif guess < secret_num:
        print("My number is higher than {}".format(guess))
      else:
        #Here give you hint if your guess number was higher the secret number.
        print("My number is lower than {}".format(guess))
#        print("That's not it!")
        #Here we want to print out hey you got it or hey you didn't get it before we append the guess.
        guesses.append(guess)
  #Let's add an else for our while above. So, else's for while's run whenever the while finishes on its own. As long as break and exception don't happen, then else will happen.
  else:
    print("You didn't get it! My numner was {}".format(secret_num))

  play_again = input("Do you want to play again? Y/N: ")
  if play_again.upper() != 'n':
    #Then lets run game again.
    game()
  else:
    print("Bye!")
  
  
game()    