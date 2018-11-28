import random
import sqlite3
import os
from datetime import date
import datetime
import math

#Nieskonczony modul 5!!!!

os.system('cls')
print("\nCzesc. Wybierz co chcesz zrobic!")


conn = sqlite3.connect('workout.db')
c = conn.cursor()

def my_db():
    # tworzenie bazy danych do programu
    c.execute('CREATE TABLE IF NOT EXISTS workoutDataBase(dzien_przemiany INTEGER, uda REAL, biceps REAL, brzuch REAL, pas REAL, klatka REAL, trening REAL, zegarek REAL, zachcianki TEXT, koszt_zachcianek REAL, interwaly REAL)')


my_db()


def data_entry():
    # dynamiczne dodawanie wartosci do bazy danych
    makeover_day = input("Ktory dzien przemiany?  ")
    os.system('cls')

    uda = float(input("Wpisz obwody uda: "))
    biceps = float(input("biceps: "))
    brzuch = float(input("brzuch: "))
    pas = float(input("pas: "))
    klatka = float(input("klatka: "))
    os.system('cls')

    trening = float(input("Czy byl dzisiaj trening? Wpisz dlugosc w minutach lub 0 jezeli dzien bez treningu < "))
    clock = float(input("Wpisz wartosc kcal z zegarka: "))
    interwaly = float(input("Wpisz ilosc minut interwalow z treningu: "))
    cravings = input("Na co dzisiaj byla ochota?  ")
    cost_cravings = float(input("Ile kosztowaloby to w zlotowkach?  "))
    os.system('cls')



    c.execute("INSERT INTO workoutDataBase(dzien_przemiany, uda, biceps, brzuch, pas, klatka, trening, zegarek, zachcianki, koszt_zachcianek, interwaly) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
    (makeover_day, uda, biceps, brzuch, pas, klatka, trening, clock, cravings, cost_cravings, interwaly))

    conn.commit()


sniadanie = ["owsianka", "tosty francuskie", "omlet", "kanapki", "jajecznica", "jajka sadzone"] # wybor rzeczy na sniadanie
II_sniadanie = ["banan", "jabłko","marchewka","shake owocowy","smoothie"] # wybor rzeczy na 2 sniadanie
kolacja = ["salatka warzywna", "salatka z tunczykiem","kanapki","warzywa"] # wybor rzeczy na kolacje

def chose_meal():
    # losowanie posilkow
    r_sniadanie = random.choice(sniadanie)
    r_II_sniadanie = random.choice(II_sniadanie)
    r_kolacja = random.choice(kolacja)
    print("\nNa sniadanie dzisiaj jest {}, na 2 sniadanie {}, a na kolacje {}".format(r_sniadanie, r_II_sniadanie, r_kolacja))


def niedobre_rzeczy():
    print("""
    1. Dodajemy cheata
    2. Przeglad cheatow

    """
    )
    cheat_wybor = int(input('> '))

    if cheat_wybor == 1:
        ktory_cheat = input("Ktory to cheat day? ")
        cheat = input("Co jadles na cheat day? ")
        with open('cheat_day.txt', 'a') as file:
            file.write('\n')
            file.write(ktory_cheat)
            file.write('\n')
            file.write(cheat)
    elif cheat_wybor == 2:
        with open('cheat_day.txt', 'r') as file:
            print(file.read())


def next_cheat_day():
    start = datetime.date(2018,9,30)
    today = datetime.date.today()
    delta = today - start
    delta_days = delta.days
    print("Jestes {} dni na diecie brawo!!".format(int(delta.days)))
    #obliczenie ile zostalo do nastepnego cheata
    next_cheat = math.ceil(delta_days/21)
    next_cheat_in_days = next_cheat * 21
    finaly_cheat_day = next_cheat_in_days - delta_days

    if delta_days %21 == 0:
        print("\nJutro cheat day!!")
    else:
        print("Zostalo {} dni do nastepnego cheata!".format(finaly_cheat_day))



while True:

    print("""

    1. Posilek na dzisiaj
    2. Dodaj obwody i trening
    3. Cheat day
    4. Kiedy nastepny cheat day?
    5. Podsumowanie cyklu
    6. Wyjscie

    """
    )

    wybor = int(input("> "))

    if wybor == 1:
        os.system('cls')
        chose_meal()
        continue
    elif wybor == 2:
        os.system('cls')
        data_entry()
        continue
    elif wybor == 3:
        os.system('cls')
        niedobre_rzeczy()
        continue
    elif wybor == 4:
        os.system('cls')
        next_cheat_day()
        continue
    elif wybor == 5:
        os.system('cls')
        pass
        continue
    elif wybor == 6:
        os.system('cls')
        break




