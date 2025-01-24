import pandas as pd
import matplotlib.pyplot as plt


def compare_champion(champion_1, champion_2):
    file_path_info = "data/interim/lolStatsFilter.csv"  
    output_file_info = "data/processed/lolStatsFilter.csv"

    df_info = pd.read_csv(file_path_info, sep=";")
    df_output_info = pd.read_csv(output_file_info, sep=";")
    """Affiche toutes les informations d'un champion."""

    champion_info1 = df_info[df_info['Name'].str.contains(champion_1, case=False, na=False)]
    champion_info2 = df_info[df_info['Name'].str.contains(champion_2, case=False, na=False)]

    if champion_info1.empty:
        print(f"Aucun champion trouvé avec le nom : {champion_1}")
    else:
        print(f"\nInformations pour le champion '{champion_1}':")
        print(champion_info1.to_string(index=False))
    
    if champion_info2.empty:
        print(f"Aucun champion trouvé avec le nom : {champion_2}")
    else:
        print(f"\nInformations pour le champion '{champion_2}':")
        print(champion_info2.to_string(index=False))
    
    combined_info = pd.concat([champion_info1, champion_info2])

    with open(output_file_info, mode="w", encoding="utf-8") as f:
        combined_info.to_csv(f, index=False, sep=";", lineterminator="\n")
        
    
    champions = df_output_info['Name'].values
    win_rates = df_output_info['Win %'].str.rstrip('%').astype(float)
    pick_rates = df_output_info['Pick %'].str.rstrip('%').astype(float)
    ban_rates = df_output_info['Ban %'].str.rstrip('%').astype(float)
    kda = df_output_info['KDA'].astype(float)
    
#
# input 
#pour test
#
    graphics_bars(champions, win_rates, 'Win %')
    graphics_circle(champions, win_rates, 'Win %')
    graphics_point(champions, win_rates, 'Win %')
    
    while True:
        choice = input("Choisissez une option : ")
        if choice == '1':
            print("ok")
        else:
            print("Au revoir !")
            break
    graphics_bars(champions, pick_rates, 'Pick %')
    graphics_circle(champions, pick_rates, 'Pick %')
    graphics_point(champions, pick_rates, 'Pick %')
    while True:
        choice = input("Choisissez une option : ")
        if choice == '1':
            print("ok")
        else:
            print("Au revoir !")
            break
    graphics_bars(champions, ban_rates, 'Ban %')
    graphics_circle(champions, ban_rates, 'Ban %')
    graphics_point(champions, ban_rates, 'Ban %')
    while True:
        choice = input("Choisissez une option : ")
        if choice == '1':
            print("ok")
        else:
            print("Au revoir !")
            break
    graphics_bars(champions, kda, 'KDA')
    graphics_circle(champions, kda, 'KDA')
    graphics_point(champions, kda, 'KDA')
    

    # choose = input("ecrit corectement ce que tu choisi entre : win_rates, pick_rates, ban_rates, kda")


def graphics_bars(champions, choose, info):

    plt.figure(figsize=(8, 6))
    plt.bar(champions, choose, color=['blue', 'green'])
    plt.title(f"{info} des Champions")
    plt.ylabel(info)
    plt.xlabel("Champions")
    plt.savefig("data/processed/win_bar_chart.png")
    plt.show()
    
def graphics_circle(champions, choose, info):

    plt.figure(figsize=(8, 6))
    plt.pie(choose, labels=champions, autopct='%1.1f%%', startangle=90, colors=['blue', 'green'])
    plt.title(f"Répartition des {info}")
    plt.savefig("data/processed/pick_pie_chart.png")
    plt.show()
    
def graphics_point(champions, choose, info):

    plt.figure(figsize=(8, 6))
    plt.scatter(champions, choose, color='purple', s=100, edgecolor='black')
    plt.title(f"{info} des Champions")
    plt.ylabel(info)
    plt.xlabel("Champions")
    plt.grid(True)
    plt.savefig("data/processed/kda_scatter_plot.png")
    plt.show()
    
    
    
    
    
    
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

if __name__ == "__main__":
    main()   
    