from random import randint

def input_function(i):
    input_number = input(f"Enter a number ({i+1}): ")
    return input_number


def wywolanie():
    lista_1 = []
    lista_2 = []
    lista_3 = []
    for i in range (6):
        while True:
            try:  #  Checking if input is of proper type
                liczba = int(input_function(i))
            except ValueError:
                print("Wrong type!")
                continue
            if 1 <= liczba <= 49: #  First checking if number is in range 1-49
                if liczba not in lista_1: #  Then checking if number has been already entered
                    lista_1.append(liczba)
                    break
                else:
                    print("Number already entered!")
            else:
                print("Number must be in range 1-49!")
    lista_1.sort()
    for _ in range (6):
        while True:
            liczba_2 = randint(1,49)
            if liczba_2 not in lista_2:
                lista_2.append(liczba_2)
                break
    lista_2.sort()
    print(f"Player's list: ", lista_1)
    print(f"Komputer's list: ", lista_2)
    for y in range (len(lista_1)):
        if lista_1[y] in lista_2:
            lista_3.append(lista_1[y])
        hits = len(lista_3)
    print(f"You have hit {hits} number(s)")


wywolanie()


