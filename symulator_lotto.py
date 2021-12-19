"""
Program asks user to enter 6 numbers in range 1-49.
Then program draw 6 random numbers in the same range and compares with user's numbers.
If there are any matching numbers, computer returns amount of hits.
"""
from random import randint

def input_function(i):
    """
    Function that receives numbers from user. In loop, executed 6 times.
    :param i: int, received from main lotto function
    :return: int
    """
    input_number = input(f"Enter a number ({i+1}): ")
    return input_number


def lotto():
    """
    Main function that exectues input_function and all other instructions
    :return: 2 lists: user's and computer's list, number of hits
    """
    lista_1 = []  # Player's list
    lista_2 = []  # Computer's list
    lista_3 = []  # List of matching numbers
    for i in range (6):
        while True:
            try:  # Checking if input is of a proper type
                liczba = int(input_function(i))
            except ValueError:
                print("Wrong type!")
                continue
            if 1 <= liczba <= 49: # First checking if number is in range 1-49
                if liczba not in lista_1: # Then checking if number has been already entered
                    lista_1.append(liczba)
                    break
                print("Number already entered!")
            else:
                print("Number must be in range 1-49!")
    lista_1.sort() # Sorting player's list ascending
    for _ in range (6): # Creating computer's list
        while True:
            liczba_2 = randint(1,49)
            if liczba_2 not in lista_2: # Checking if there are no two identical values in the list
                lista_2.append(liczba_2)
                break
    lista_2.sort() # Sorting computer's list
    print("Player's list: ", lista_1)
    print("Computer's list: ", lista_2)
    for number in lista_1: # Cheking for hits
        if number in lista_2:
            lista_3.append(number)
        hits = len(lista_3)
    print(f"You have hit {hits} number(s)")


lotto()
