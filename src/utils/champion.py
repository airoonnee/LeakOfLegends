import pandas as pd
import os

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../data')
DATA_DIR = os.path.abspath(BASE_DIR)

file_spell = "championFullFilter.csv"  
output_file_spell = "championFullFilter.csv"

def detail_champion(champion_name):
    """Affiche toutes les informations d'un champion."""
    file_path_spell = os.path.join(DATA_DIR, 'interim', file_spell)
    output_file_spell_path = os.path.join(DATA_DIR, 'processed', output_file_spell)

    df_spell = pd.read_csv(file_path_spell, sep=";")

    champion_details = df_spell[df_spell['name'] == champion_name]
    
    with open(output_file_spell_path, mode="w", encoding="utf-8") as f:
        champion_details.to_csv(f, index=False, sep=";", lineterminator="\n")
