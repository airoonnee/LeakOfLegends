import pandas as pd
from champion import Champion

def main():
    print("Menu:")
    print("1. Afficher les informations d'un champion")

    print("6. Quitter")

    while True:
        choice = input("Choisissez une option : ")

        if choice == '1':
            champion_name = input("Entrez le nom du champion : ")
            Champion.afficher_info_champion(champion_name)
        else:
            print("Au revoir !")
            break

# Lancer le programme
if __name__ == "__main__":
    main()