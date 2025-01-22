import pandas as pd
import keyboard  # Installation avec `pip install keyboard`

# Charger le fichier CSV
file_path = "data/test.csv"  # Remplacez par le chemin de votre fichier CSV
try:
    data = pd.read_csv(file_path)
except FileNotFoundError:
    print(f"Le fichier {file_path} n'a pas été trouvé.")
    exit()

# Vérifier la colonne contenant les noms des champions
if "Champion" not in data.columns:
    print("La colonne 'Champion' n'est pas présente dans le fichier.")
    exit()

# Variable globale pour stocker la recherche
search_query = ""

def search_champion(query):
    """Recherche les champions correspondant à la requête."""
    if query.strip() == "":  # Si la recherche est vide, afficher tous les champions
        print("\rListe complète des champions :")
        print(data['Champion'].to_string(index=False))
    else:
        results = data[data['Champion'].str.contains(query, case=False, na=False)]
        if results.empty:
            print(f"\rAucun champion trouvé pour : '{query}'", end="")
        else:
            print(f"\n\rChampions trouvés pour '{query}': {', '.join(results['Champion'])}", end="")

def on_key_event(e):
    """Déclenche la recherche à chaque frappe de touche."""
    global search_query
    if e.name == "backspace":
        search_query = search_query[:-1]  # Supprimer le dernier caractère
    elif e.name == "enter":
        print("\nRecherche terminée.")
        keyboard.unhook_all()  # Arrêter d'écouter les événements
    elif len(e.name) == 1:  # Ajouter les lettres ou chiffres
        search_query += e.name
    search_champion(search_query)

print("Tapez au fur et à mesure pour rechercher un champion (Appuyez sur 'Entrée' pour quitter) :")
keyboard.on_press(on_key_event)  # Attache la fonction `on_key_event` aux frappes de touches
keyboard.wait("enter")  # Bloque le programme jusqu'à ce que "Entrée" soit pressé
