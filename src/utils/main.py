import pandas as pd
from compare import Compare

def main():
    print("Menu:")
    print("1. Afficher les informations d'un champion")

    print("2. Quitter")

    while True:
        choice = input("Choisissez une option : ")

        if choice == '1':
            champion_1 = input("Entrez le nom du champion 1 : ")
            champion_2 = input("Entrez le nom du champion 2 : ")

            compare_champion(champion_1, champion_2)
        else:
            print("Au revoir !")
            break

# Lancer le programme
if __name__ == "__main__":
    main()