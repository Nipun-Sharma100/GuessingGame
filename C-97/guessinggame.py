import random
 
number = random.randrange(1, 10)
 
guess = int(input("Please enter your guess: "))
 
if guess == number:
    print ("Correct!")
elif guess < number:
    print ("Your guess is too low")
else:
    print ("Your guess is too high")