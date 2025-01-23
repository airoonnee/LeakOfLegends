import pandas as pd
import sys
import os

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../data')
DATA_DIR = os.path.abspath(BASE_DIR)
input_file = 'lolStatsFilter.csv'
output_file = 'lolStatsFilter.csv'

def filtrer_par_role(input_file, output_file, role):
    input_path = os.path.join(DATA_DIR, 'interim', input_file)
    output_path = os.path.join(DATA_DIR, 'processed', output_file)

    df = pd.read_csv(input_path, delimiter=';')
    
    df_filtre = df[df['Role'] == role]
    
    df_filtre.to_csv(output_path, index=False, sep=';')
    
    print(df_filtre[['Name', 'Class', 'Role', 'Tier', 'Win %', 'Pick %', 'Ban %', 'KDA']])

def filtrer_par_classe(input_file, output_file, classe):
    input_path = os.path.join(DATA_DIR, 'interim', input_file)
    output_path = os.path.join(DATA_DIR, 'processed', output_file)

    df = pd.read_csv(input_path, delimiter=';')
    
    df_filtre = df[df['Class'] == classe]
    
    df_filtre.to_csv(output_path, index=False, sep=';')
    
    print(df_filtre[['Name', 'Class', 'Role', 'Tier', 'Win %', 'Pick %', 'Ban %', 'KDA']])

def filtrer_par_tier(input_file, output_file, tier):
    input_path = os.path.join(DATA_DIR, 'interim', input_file)
    output_path = os.path.join(DATA_DIR, 'processed', output_file)

    df = pd.read_csv(input_path, delimiter=';')
    
    df_filtre = df[df['Tier'] == tier]
    
    df_filtre.to_csv(output_path, index=False, sep=';')
    
    print(df_filtre[['Name', 'Class', 'Role', 'Tier', 'Win %', 'Pick %', 'Ban %', 'KDA']])

if __name__ == "__main__":
    filtre = 'role'
    valeur = 'ADC'

    if filtre == 'role':
        filtrer_par_role(input_file, output_file, valeur)
    elif filtre == 'classe':
        filtrer_par_classe(input_file, output_file, valeur)
    elif filtre == 'tier':
        filtrer_par_tier(input_file, output_file, valeur)