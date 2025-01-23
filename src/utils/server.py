import http.server
import socketserver
import os
import csv
import json
from urllib.parse import urlparse, parse_qs
from tries import trier_par_nom_asc, trier_par_nom_desc, trier_par_classe_asc, trier_par_classe_desc, trier_par_role_asc, trier_par_role_desc, trier_par_tier_asc, trier_par_tier_desc, trier_par_win_asc, trier_par_win_desc, trier_par_pick_asc, trier_par_pick_desc, trier_par_ban_asc, trier_par_ban_desc, trier_par_kda_asc, trier_par_kda_desc
from filtre import reset, filtrer_par_role, filtrer_par_tier, filtrer_par_classe

PORT = 8000

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, '../templates')
STATIC_DIR = os.path.join(BASE_DIR, '../static')
DATA_DIR = os.path.join(BASE_DIR, '../../data/processed')

class SimpleHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self._serve_file(os.path.join(TEMPLATES_DIR, 'index.html'))
        elif self.path == '/champions':
            self._serve_file(os.path.join(TEMPLATES_DIR, 'champions.html'))
        elif self.path == '/api/lol-stats':
            reset('lolStatsFilter.csv', 'lolStatsFilter.csv')
            self._serve_csv(os.path.join(DATA_DIR, 'lolStatsFilter.csv'))
        elif self.path.startswith('/api/sort'):    
            input_file = 'lolStatsFilter.csv'
            output_file = 'lolStatsFilter.csv'

            query = parse_qs(urlparse(self.path).query)
            column = query.get('column', [''])[0]
            order = query.get('order', ['ASC'])[0]

            if column == "Name" and order == 'ASC' :
                trier_par_nom_asc(input_file, output_file)
            elif column == "Name" and order == 'DESC':
                trier_par_nom_desc(input_file, output_file)
            elif column == "Class" and order == 'ASC' :
                trier_par_classe_asc(input_file, output_file)
            elif column == "Class" and order == 'DESC':
                trier_par_classe_desc(input_file, output_file)
            elif column == "Role" and order == 'ASC' :
                trier_par_role_asc(input_file, output_file)
            elif column == "Role" and order == 'DESC':
                trier_par_role_desc(input_file, output_file)
            elif column == "Tier" and order == 'ASC' :
                trier_par_tier_asc(input_file, output_file)
            elif column == "Tier" and order == 'DESC':
                trier_par_tier_desc(input_file, output_file)
            elif column == "Win" and order == 'ASC' :
                trier_par_win_asc(input_file, output_file)
            elif column == "Win" and order == 'DESC':
                trier_par_win_desc(input_file, output_file)
            elif column == "Pick" and order == 'ASC' :
                trier_par_pick_asc(input_file, output_file)
            elif column == "Pick" and order == 'DESC':
                trier_par_pick_desc(input_file, output_file)
            elif column == "Ban" and order == 'ASC' :
                trier_par_ban_asc(input_file, output_file)
            elif column == "Ban" and order == 'DESC':
                trier_par_ban_desc(input_file, output_file)
            elif column == "KDA" and order == 'ASC' :
                trier_par_kda_asc(input_file, output_file)
            elif column == "KDA" and order == 'DESC':
                trier_par_kda_desc(input_file, output_file)

            output_path = os.path.join(DATA_DIR, output_file)
            with open(output_path, 'r') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=';')
                sorted_data = [row for row in reader]

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(sorted_data).encode('utf-8'))
        elif self.path.startswith('/api/filter'):    
            input_file = 'lolStatsFilter.csv'
            output_file = 'lolStatsFilter.csv'

            query = parse_qs(urlparse(self.path).query)
            column = query.get('column', [''])[0]
            value = query.get('value', [''])[0]

            if column == "Role" :
                filtrer_par_role(input_file, output_file, value)
            elif column == "Tier" : 
                filtrer_par_tier(input_file, output_file, value)
            elif column == "Class" :
                filtrer_par_classe(input_file, output_file, value)

            output_path = os.path.join(DATA_DIR, output_file)
            with open(output_path, 'r') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=';')
                sorted_data = [row for row in reader]

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(sorted_data).encode('utf-8'))
        else:
            static_path = os.path.join(STATIC_DIR, self.path.lstrip('/'))
            if os.path.exists(static_path):
                self._serve_file(static_path)

    def _serve_file(self, file_path):
        if os.path.exists(file_path):
            self.send_response(200)
            if file_path.endswith(".html"):
                self.send_header("Content-type", "text/html")
            elif file_path.endswith(".css"):
                self.send_header("Content-type", "text/css")
            else:
                self.send_header("Content-type", "application/octet-stream")
            self.end_headers()
            with open(file_path, 'rb') as f:
                self.wfile.write(f.read())
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"<h1>404 Not Found</h1><p>Fichier introuvable.</p>")

    def _serve_csv(self, file_path):
        if os.path.exists(file_path):
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            with open(file_path, 'r') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=';') 
                data = [row for row in reader]
                self.wfile.write(json.dumps(data).encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "CSV file not found"}).encode('utf-8'))


with socketserver.TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
    print(f"Serveur démarré sur le port {PORT}")
    httpd.serve_forever()
