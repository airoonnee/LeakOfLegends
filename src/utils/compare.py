import pandas as pd
import matplotlib.pyplot as plt
import os

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../data')
DATA_DIR = os.path.abspath(BASE_DIR)

file_info = "lolStatsFilter.csv"  
output_file_spell = "lolStatsFilter.csv"

def compare_champion(champion_1, champion_2, forme):
    file_path_info = os.path.join(DATA_DIR, 'interim', file_info)
    output_file_info = os.path.join(DATA_DIR, 'processed', output_file_spell)

    df_info = pd.read_csv(file_path_info, sep=";")

    champion_info1 = df_info[df_info['Name'] == champion_1]
    champion_info2 = df_info[df_info['Name'] == champion_2]

    champion_info1 = champion_info1.drop_duplicates(subset='Name')
    champion_info2 = champion_info2.drop_duplicates(subset='Name')

    combined_info = pd.concat([champion_info1, champion_info2])

    with open(output_file_info, mode="w", encoding="utf-8") as f:
        combined_info.to_csv(f, index=False, sep=";", lineterminator="\n")

    df_output_info = pd.read_csv(output_file_info, sep=";")

    champions = df_output_info['Name'].values
    win_rates = df_output_info['Win %'].str.rstrip('%').astype(float)
    pick_rates = df_output_info['Pick %'].str.rstrip('%').astype(float)
    ban_rates = df_output_info['Ban %'].str.rstrip('%').astype(float)
    kda = df_output_info['KDA'].astype(float)
    
    if forme == "Barre":
        graphics_bars(champions, win_rates, 'Win%', champion_1, champion_2)
        graphics_bars(champions, pick_rates, 'Pick%', champion_1, champion_2)
        graphics_bars(champions, ban_rates, 'Ban%', champion_1, champion_2)
        graphics_bars(champions, kda, 'KDA', champion_1, champion_2)
    
    elif forme == "Cercle":
        graphics_circle(champions, win_rates, 'Win%', champion_1, champion_2)
        graphics_circle(champions, pick_rates, 'Pick%', champion_1, champion_2)
        graphics_circle(champions, ban_rates, 'Ban%', champion_1, champion_2)
        graphics_circle(champions, kda, 'KDA', champion_1, champion_2)

    elif forme == "Point":  
        graphics_point(champions, win_rates, 'Win%', champion_1, champion_2)
        graphics_point(champions, pick_rates, 'Pick%', champion_1, champion_2)
        graphics_point(champions, ban_rates, 'Ban%', champion_1, champion_2)
        graphics_point(champions, kda, 'KDA', champion_1, champion_2)

def graphics_bars(champions, choose, info, champion_1, champion_2):
    file_path = f"src/static/img/{champion_1}_{champion_2}_bar_{info}.png"
    plt.figure(figsize=(8, 6))
    plt.bar(champions, choose, color=['blue', 'green'])
    plt.title(f"{info} des Champions")
    plt.ylabel(info)
    plt.xlabel("Champions")
    plt.savefig(file_path)
    
def graphics_circle(champions, choose, info, champion_1, champion_2):
    file_path = f"src/static/img/{champion_1}_{champion_2}_circle_{info}.png"
    plt.figure(figsize=(8, 6))
    plt.pie(choose, labels=champions, autopct='%1.1f%%', startangle=90, colors=['blue', 'green'])
    plt.title(f"Répartition des {info}")
    plt.savefig(file_path)
    
def graphics_point(champions, choose, info, champion_1, champion_2):
    file_path = f"src/static/img/{champion_1}_{champion_2}_point_{info}.png"
    plt.figure(figsize=(8, 6))
    plt.scatter(champions, choose, color='purple', s=100, edgecolor='black')
    plt.title(f"{info} des Champions")
    plt.ylabel(info)
    plt.xlabel("Champions")
    plt.grid(True)
    plt.savefig(file_path)