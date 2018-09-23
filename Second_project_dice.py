import random

welcome = "Welcome to random dice roller. Follow the instructions and have fun!!\n\n"
done = False
print(welcome)
num_min = 1
num_max = 6


while not done:
    choice = input("\nType [roll] to roll a number or type [quit] to exit The Dice: ")
    choice.lower()
    if choice == 'roll':
        dice = random.randint(num_min, num_max)
        print("\nThats your number: ", dice)
    elif choice == 'quit':
        print("Bye Bye :) ")
        done = True
    else:
        print("Follow instructions God damn it!!!")

