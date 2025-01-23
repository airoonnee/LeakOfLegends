import pandas as pd
import keyboard  

file_path = "data/test.csv"  
try:
    data = pd.read_csv(file_path, sep=";")
except FileNotFoundError:
    print(f"Le fichier {file_path} n'a pas été trouvé.")
    exit()

if "Name" not in data.columns:
    print("La colonne 'Name' n'est pas présente dans le fichier.")
    exit()

search_query = ""

def search_champion(query):
    """Recherche les names correspondant à la requête."""
    if query.strip() == "":  
        print("\rListe complète des names :")
        print(data['Name'].to_string(index=False))
    else:
        results = data[data['Name'].str.contains(query, case=False, na=False)]
        if results.empty:
            print(f"\rAucun name trouvé pour : '{query}'", end="")
        else:
            print(f"\n\rNames trouvés pour '{query}': {', '.join(results['Name'])}", end="")

def on_key_event(e):
    """Déclenche la recherche à chaque frappe de touche."""
    global search_query
    if e.name == "backspace":
        search_query = search_query[:-1]  
    elif e.name == "enter":
        print("\nRecherche terminée.")
        keyboard.unhook_all()  
    elif len(e.name) == 1:  
        search_query += e.name
    search_champion(search_query)

print("Tapez au fur et à mesure pour rechercher un name (Appuyez sur 'Entrée' pour quitter) :")
keyboard.on_press(on_key_event)  
keyboard.wait("enter")  
