import pandas as pd
import os
import sys

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../data')
DATA_DIR = os.path.abspath(BASE_DIR)

def trier_par_nom_asc(input_file, output_file):
    trier_par_critere(input_file, output_file, 'Name', 'ASC')

def trier_par_nom_desc(input_file, output_file):
    trier_par_critere(input_file, output_file, 'Name', 'DESC')

def trier_par_classe_asc(input_file, output_file):
    trier_par_critere(input_file, output_file, 'Class', 'ASC')

def trier_par_classe_desc(input_file, output_file):
    trier_par_critere(input_file, output_file, 'Class', 'DESC')

def trier_par_role_asc(input_file, output_file):
    trier_par_critere(input_file, output_file, 'Role', 'ASC')

def trier_par_role_desc(input_file, output_file):
    trier_par_critere(input_file, output_file, 'Role', 'DESC')

def trier_par_tier_asc(input_file, output_file):
    trier_par_critere(input_file, output_file, 'Tier', 'ASC')

def trier_par_tier_desc(input_file, output_file):
    trier_par_critere(input_file, output_file, 'Tier', 'DESC')

def trier_par_win_asc(input_file, output_file):
    trier_par_critere(input_file, output_file, 'Win %', 'ASC')

def trier_par_win_desc(input_file, output_file):
    trier_par_critere(input_file, output_file, 'Win %', 'DESC')

def trier_par_pick_asc(input_file, output_file):
    trier_par_critere(input_file, output_file, 'Pick %', 'ASC')

def trier_par_pick_desc(input_file, output_file):
    trier_par_critere(input_file, output_file, 'Pick %', 'DESC')

def trier_par_ban_asc(input_file, output_file):
    trier_par_critere(input_file, output_file, 'Ban %', 'ASC')

def trier_par_ban_desc(input_file, output_file):
    trier_par_critere(input_file, output_file, 'Ban %', 'DESC')

def trier_par_kda_asc(input_file, output_file):
    trier_par_critere(input_file, output_file, 'KDA', 'ASC')

def trier_par_kda_desc(input_file, output_file):
    trier_par_critere(input_file, output_file, 'KDA', 'DESC')

def trier_par_critere(input_file, output_file, critere, ordre='ASC'):
    input_path = os.path.join(DATA_DIR, 'processed', input_file)
    output_path = os.path.join(DATA_DIR, 'processed', output_file)
    
    df = pd.read_csv(input_path, delimiter=';')

    if critere == 'Tier':
        custom_order = {'God': 0, 'S': 1, 'A': 2, 'B': 3, 'C': 4, 'D': 5}
        if ordre == 'ASC':
            df_trie = df.sort_values(by=critere, key=lambda x: x.map(custom_order))
        else:
            df_trie = df.sort_values(by=critere, key=lambda x: x.map(custom_order), ascending=False)
    else:
        if ordre == 'ASC':
            df_trie = df.sort_values(by=critere, ascending=True)
        else:
            df_trie = df.sort_values(by=critere, ascending=False)
            
    df_trie.to_csv(output_path, index=False, sep=';')
    print(df_trie)
