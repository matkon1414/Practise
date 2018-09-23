import random

"""
Dzikusy zawsze poruszaja sie od 5 - 10 mil, zmeczenie to przedzial od 1 do 3, fullspeed to zawsze jest od 10 do 20 mil, sredni speed to jest od 5 do 12 konczymy gre jezeli pragnienie wyzsze niz 7 a zmeczenie wyzsze niz 8. Konczymy gre jezeli przebiegniemy cala pustynie tj(210 mil)

"""
welcome_text = "Welcome to Camel!\nYou have stolen a camel to make your way across the Great Mobi desert which is 210 miles long.The natives want their camel back and are chasing you down!Survive your desert trek and out run the natives!!\n\n\n"
print(welcome_text)  # drukuje teskt na poczatku
done = False
miles_traveled = 0
thirst = 0
camel_tiredness = 0
natives_travel = -20
canteen_drinks = 3
oasis = 5
while not done:
    answers = "-------------------------------------\nA. Drink from your canteen.\nB. Ahead moderate speed.\nC. Ahead full speed.\nD. Stop for the night.\nE. Status check.\nQ. Quit.\n"
    print(answers)  # pierwsze odpowiedzi
    distance_differenial = natives_travel - miles_traveled
    answer1 = input("--------------\nYour choice: ")
    answer1 = answer1.upper()
 # print("Answer: ", answer1) testuje czy zwieksza odpowiedz
    if answer1 == 'Q':  # wyjscie z gry
        are_you_sure = input("Are you sure? Type: [y - quit] or [any key to continue]  ")
        are_you_sure.lower()
        if are_you_sure == 'y':
            done = True
        else:
            done = False
    elif answer1 == 'E':    # bierzace informacje
        # distance_differenial = natives_travel - miles_traveled
        print("\nMiles traveled: ", miles_traveled, "\nThe natives are ", abs(distance_differenial), " behind\n", "Thirst: ", thirst, "\nCamel tiredness: ", camel_tiredness)
        if canteen_drinks <= 0:
            print("You are out of drinks!!")
        else:
            print("\nDrinks in canteen: ", canteen_drinks)
        if abs(distance_differenial) <= 15:
            print("\n\nThey are getting closer!! Be carefull!!")
    elif answer1 == 'D':    # odpoczynek, ale dzikusy sa blizej
        print("\nCamel is happy and rested!")
        natives_travel = natives_travel + random.randrange(5, 11)
        camel_tiredness = 0
        # print(natives_travel)
    elif answer1 == 'C':    # full speed
        full_speed_miles = random.randrange(10, 21)
        miles_traveled = miles_traveled + full_speed_miles
        print("\nYou travel for: ", full_speed_miles, " miles")
        thirst += 1
        # print(thirst)
        camel_tiredness = camel_tiredness + random.randrange(1, 4)
        # print (camel_tiredness)
        natives_travel = natives_travel + random.randrange(5, 11)
        # print(natives_travel)
    elif answer1 == 'B':  # sredni speed
        moderate_speed_miles = random.randrange(5, 13)
        miles_traveled = miles_traveled + moderate_speed_miles
        print("\nYou travel for: ", moderate_speed_miles, " miles")
        thirst += 1
        # print(thirst)
        camel_tiredness += 1
        # print(camel_tiredness)
        natives_travel = natives_travel + random.randrange(5, 11)
    elif answer1 == 'A':  # picie z buklaku
        if canteen_drinks >= 1:
            canteen_drinks -= 1
            thirst = 0
        else:
            print("You are out of drinks!!")
    if thirst >= 4 and thirst <= 6:
        print("\n\nYou are thirsty!!Drink up!!")
        print("Thirst: ", thirst)
    if camel_tiredness >= 5 and camel_tiredness <= 8:
        print("\n\nYour camel is tired! Please take a rest")
        print("\nCamel tiredness: ", camel_tiredness)
    if thirst > 6:  # jedna rzecz konczy gre dlatego if i elify
        print("\n\nYou died of thirst!! Game Over :((")
        done = True
        print("\nMiles traveled: ", miles_traveled, "\nThe natives are ", abs(distance_differenial), " behind\n", "Thirst: ", thirst, "\nCamel tiredness: ", camel_tiredness)
    elif camel_tiredness > 8:
        print("\n\nYour camel died of tiredness!! Next time take some rest!")
        done = True
        print("\nMiles traveled: ", miles_traveled, "\nThe natives are ", abs(distance_differenial), " behind\n", "Thirst: ", thirst, "\nCamel tiredness: ", camel_tiredness)
    elif natives_travel >= miles_traveled:
        print("\n\nNatives got you. You are dead!")
        done = True
        print("\nMiles traveled: ", miles_traveled, "\nThe natives are ", abs(distance_differenial), " behind\n", "Thirst: ", thirst, "\nCamel tiredness: ", camel_tiredness)
    elif miles_traveled >= 210 and natives_travel < miles_traveled:
        print("\n\nCongratulation!! Your camel outrunned stupid natives!! You Escaped!!")
        done = True
        print("\nMiles traveled: ", miles_traveled, "\nThe natives are ", abs(distance_differenial), " behind\n", "Thirst: ", thirst, "\nCamel tiredness: ", camel_tiredness)
    if random.randrange(0, 101) == oasis:
        print("\n\nWhat a miracle!! You found oasis!! You feel rested")
        canteen_drinks = 3
        thirst = 0
        camel_tiredness = 0
        print("\nMiles traveled: ", miles_traveled, "\nThe natives are ", abs(distance_differenial), " behind\n", "Thirst: ", thirst, "\nCamel tiredness: ", camel_tiredness)
    # break
