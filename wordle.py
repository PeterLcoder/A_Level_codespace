import requests #this is to import from the word generator
from colorama import Fore #colours


def lettercheck(word , guess):                      #the lettercheck function
    global guesses                                  #globalise guesses
    for i in range(5):                              #loops for the number of letters (5)
        if len(guess) != 5:                         #validity check
            print(f"{guess} is not 5 letters")
            guesses = guesses +1                    #neutralises guesses count so the invalid doesn't take from guesses
            break                                   #makes sure invalid message doesn't print 5 times
        elif guess[i] == word[i]:                   #green check
            print(Fore.GREEN, guess[i], end="")
        elif guess[i] in word:                      #yellow check
            print(Fore.YELLOW, guess[i], end="")
        elif guess[i] != word[i]:                   #red check
            print(Fore.RED, guess[i], end="")
    print("")

    guesses = guesses-1                             #increments function

    if guess == word:                               #win
        print("you did it!")
        guesses = 0
    elif guess != word and guesses == 0:                            #lose
        print(f'the word was {word}, better luck next time')

playing = True

while playing:
    word = requests.get(f'https://random-word-api.vercel.app/api?words=1&length=5')    #import random word
    if word.status_code == 200:
        word = str(*word.json())

    guesses = 6 #variable that the while loop is dependent on

    while guesses != 0:                                        #begins the whole game loop
        guess = input("input your guess:  ")
        lettercheck(word , guess)
    
    replay = input("would you like to play again? (Y/N):  ")   #replay
    if replay == "N":
        playing = False


