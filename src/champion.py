import pandas as pd

df = "data/test.csv"  
output_file = "data/top_results.csv"

class Champion:
    def afficher_info_champion(df, champion_name):
        """Affiche toutes les informations d'un champion."""

        champion_info = df[df['Name'].str.contains(champion_name, case=False, na=False)]
        
        if champion_info.empty:
            print(f"Aucun champion trouvé avec le nom : {champion_name}")
        else:
            print(f"\nInformations pour le champion '{champion_name}':")
            print(champion_info.to_string(index=False))
        
        with open(output_file, mode="w", encoding="utf-8") as f:
            champion_info.to_csv(f, index=False, sep=";", lineterminator="\n")

