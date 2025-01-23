import pandas as pd
import os

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../data')
DATA_DIR = os.path.abspath(BASE_DIR)

def search(input_file, output_file, query):
    input_path = os.path.join(DATA_DIR, 'interim', input_file)
    output_path = os.path.join(DATA_DIR, 'processed', output_file)

    df = pd.read_csv(input_path, delimiter=';')

    results = df[df['Name'].str.contains(query, case=False, na=False)]

    results.to_csv(output_path, index=False, sep=';')