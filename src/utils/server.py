import http.server
import socketserver
import os
import csv
import json

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
            self._serve_csv(os.path.join(DATA_DIR, 'lolStatsFilter.csv'))
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
