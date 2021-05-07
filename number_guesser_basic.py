# Number guessing game
# first python project


import random

score = 100
print ('score: ' + str(score))

num = random.randint(1, 100)
guess = input('Guess a number 1 through 100: ')

while guess != num:
    score -= 10
    print ('score: ' + str(score))
    if int(guess) < num:
        print (str(guess) + " is too low!")
        guess = input('Guess again: ')
    elif int(guess) > num:   
        print (str(guess) + " is too high!")
        guess = input("Guess again: ")
    else:
        break
    
print ("Congratulations, you guessed correctly!")
    
