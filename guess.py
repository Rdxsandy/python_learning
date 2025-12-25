# we are trt to code a guess game in which we will tell that user is worn of not and try ot correct him
import random

guess = -1
choosen = 1

while guess != choosen:
    guess = int(random.random() * 100)
    print(guess)
    choosen = int(input("please enter the number"))
    if guess == choosen:
        print("you perfectly guess the number")
    elif guess>choosen:
        print("guess lower")
    else:    
        print("guess higher")
    