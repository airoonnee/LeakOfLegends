import pandas as pd
import sys

def filtrer_par_role(input_file, output_file, role):
    # Lire le fichier CSV
    df = pd.read_csv(input_file, delimiter=';')
    
    # Filtrer les données par rôle
    df_filtre = df[df['Role'] == role]
    
    # Écrire les données filtrées dans un nouveau fichier CSV
    df_filtre.to_csv(output_file, index=False, sep=';')
    
    # Afficher les données filtrées
    print(df_filtre[['Name', 'Class', 'Role', 'Tier', 'Win %', 'Pick %', 'Ban %', 'KDA']])

def filtrer_par_classe(input_file, output_file, classe):
    # Lire le fichier CSV
    df = pd.read_csv(input_file, delimiter=';')
    
    # Filtrer les données par classe
    df_filtre = df[df['Class'] == classe]
    
    # Écrire les données filtrées dans un nouveau fichier CSV
    df_filtre.to_csv(output_file, index=False, sep=';')
    
    # Afficher les données filtrées
    print(df_filtre[['Name', 'Class', 'Role', 'Tier', 'Win %', 'Pick %', 'Ban %', 'KDA']])

def filtrer_par_tier(input_file, output_file, tier):
    # Lire le fichier CSV
    df = pd.read_csv(input_file, delimiter=';')
    
    # Filtrer les données par tier
    df_filtre = df[df['Tier'] == tier]
    
    # Écrire les données filtrées dans un nouveau fichier CSV
    df_filtre.to_csv(output_file, index=False, sep=';')
    
    # Afficher les données filtrées
    print(df_filtre[['Name', 'Class', 'Role', 'Tier', 'Win %', 'Pick %', 'Ban %', 'KDA']])

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    filtre = sys.argv[3]
    valeur = sys.argv[4]
    
    if filtre == 'role':
        filtrer_par_role(input_file, output_file, valeur)
    elif filtre == 'classe':
        filtrer_par_classe(input_file, output_file, valeur)
    elif filtre == 'tier':
        filtrer_par_tier(input_file, output_file, valeur)