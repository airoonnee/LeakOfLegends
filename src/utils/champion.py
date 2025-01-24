import pandas as pd

file_path_info = "data/interim/lolStatsFilter.csv"  
output_file_info = "data/processed/lolStatsFilter.csv"

file_path_spell = "data/interim/championFullFilter.csv"  
output_file_spell = "data/processed/championFullFilter.csv"

df_info = pd.read_csv(file_path_info, sep=";")
df_spell = pd.read_csv(file_path_spell, sep=";")

class Champion:
    def detail_champion(champion_name):
        """Affiche toutes les informations d'un champion."""

        champion_info = df_info[df_info['Name'].str.contains(champion_name, case=False, na=False)]
        champion_spell = df_spell[df_spell['name'].str.contains(champion_name, case=False, na=False)]

        if champion_info.empty:
            print(f"Aucun champion trouvé avec le nom : {champion_name}")
        else:
            print(f"\nInformations pour le champion '{champion_name}':")
            print(champion_info.to_string(index=False))
        
        with open(output_file_info, mode="w", encoding="utf-8") as f:
            champion_info.to_csv(f, index=False, sep=";", lineterminator="\n")

        if champion_spell.empty:
            print(f"Aucun champion trouvé avec le nom : {champion_name}")
        else:
            print(f"\nInformations pour le champion '{champion_name}':")
            print(champion_spell.to_string(index=False))
        
        with open(output_file_spell, mode="w", encoding="utf-8") as f:
            champion_spell.to_csv(f, index=False, sep=";", lineterminator="\n")