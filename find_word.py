#gra polega na odnalezieniu w podanych slowach innych slow.


import random as rd
WORDS = ("treehouse", "spiderman","VisualStudioCode") #podane wyrazy

random_word = rd.choice(WORDS)
print("Welcome to find words game!!\n\n")


def game_mode(playable_word):   #funkcja liczaca ilosc slow oraz zapisujaca slowa
    guesses = set()
    print("Find as many words as you can in word: " + playable_word + ". \nFor exit type (Q)\n\n")
    while True:
        choice = input("<< {}    ".format(len(guesses)+1))
        if choice.lower() == 'q':
            break
        guesses.add(choice)
    return guesses


player_1 = game_mode(random_word) #rozgrywka gracza 1
print("-"*10)
print("Thank you player_1. Now it is turn for player_2\n") #rozgrywka gracza 2
player_2 = game_mode(random_word)

print("Player_1 found {} words end player_2 {} words\n".format(len(player_1), len(player_2))) #podsumowanie rozgrywki
the_same_words = player_1 & player_2
print("The same words that you find: ", the_same_words) #ilosc tych samych slow

unique_words_1 = player_1 - player_2 #unikalne slowa dla gracza 1
unique_words_2 = player_2 - player_1 #unikalne slowa dla gracza 2
if len(unique_words_1) == 0:
    unique_words_1 = None
if len(unique_words_2) == 0:
    unique_words_2 = None
print("Unique words for player_1: ", unique_words_1, "\nUnique words for player_2: ", unique_words_2)

