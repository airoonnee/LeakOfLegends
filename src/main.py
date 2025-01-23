import pandas as pd
from top import Top
from champion import Champion

def main():
    file_path = "data/test.csv"
    df = pd.read_csv(file_path, sep=";")
    nbr_input = input("top 10, 20, 50, 100 \nÉcrivez le nombre de résultats souhaités : ")
    nbr = int(nbr_input)

    print("Menu:")
    print("1. Top champions par Win %")
    print("2. Top champions par Pick %")
    print("3. Top champions par Ban %")
    print("4. Top champions par KDA")
    print("5. Afficher les informations d'un champion")

    print("6. Quitter")

    while True:
        choice = input("Choisissez une option (1-6) : ")

        if choice == '1':
            Top.top(df, nbr, 'Win %')
        elif choice == '2':
            Top.top(df, nbr, 'Pick %')
        elif choice == '3':
            Top.top(df, nbr, 'Ban %')
        elif choice == '4':
            Top.top(df, nbr, 'KDA')
        elif choice == '5' :
            champion_name = input("Entrez le nom du champion : ")
            Champion.afficher_info_champion(df, champion_name)
        elif choice == '6':
            print("Au revoir !")
            break
        else:
            print("Option invalide. Veuillez entrer un nombre entre 1 et 5.")

# Lancer le programme
if __name__ == "__main__":
    main()