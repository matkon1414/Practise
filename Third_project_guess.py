import random
from time import sleep
import os


loop = False
welcome = "Welcome to game called ""Guess what number I think of"". You need to take a guess what number computer generates form 1 to 100. Try to do it in small amount of tries. Have fun!!\n\n"
print(welcome)

while not loop:  # glowna petla

    number = random.randint(1, 100)  # generowanie liczby do zgadywania
    #print(number)
    done = False
    i = 0
    print("\nOK. I'm ready!\n")

    while not done:
        guess = input("\nPlease take a shot and guess the number i think: ")
        must_be_int = guess.isdigit()  # sprawdzanie czy wpisana odp jest int
        if must_be_int == True:
            guess_int = int(guess)
            guess = guess_int
            if guess > number:
                print("\nTo high! Try again!")
                sleep(1)
                os.system('cls')
            elif guess < number:
                print("\nTo low son! Try again")
                sleep(1)
                os.system('cls')
            elif guess == number:
                print("\nYou got me pall!. It was easy right?")
                done = True
            i += 1
        else:  # jezeli nie to sprobuj ponownie
            print("Type digits pal!")
            continue

    if i == 1:
        print("On the first time???? Are you kidding me??? Guess you are lucky :)\n ")  # jezeli za pierwszym razem
    else:
        print("This time it took ", i, " times to beat me!\n")
    print("Do you wanna try me again?")  # pytanie o ponowna gre
    ending = False
    while not ending:
        again = input("\nType [y] to continue or [n] to exit :")
        again.lower()
        if again == 'y':
            done = False
            ending = True
        elif again == 'n':
            loop = True
            ending = True
            print("\n\nBye! I hope you had fun. To the next time!")
        else:
            print("Please follow instructions!!\n")
            continue
