import pandas as pd
import sys

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
    # Lire le fichier CSV
    df = pd.read_csv(input_file, delimiter=';')
    
    # Trier les données par le critère spécifié
    if ordre == 'ASC':
        df_trie = df.sort_values(by=critere, ascending=True)
    else:
        df_trie = df.sort_values(by=critere, ascending=False)
    
    # Écrire les données triées dans un nouveau fichier CSV
    df_trie.to_csv(output_file, index=False, sep=';')
    
    # Afficher les données triées
    print(df_trie)

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    critere = sys.argv[3]
    ordre = sys.argv[4]
    trier_par_critere(input_file, output_file, critere, ordre)