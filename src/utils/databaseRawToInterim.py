import os
import json
import pandas as pd

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../data')
DATA_DIR = os.path.abspath(BASE_DIR)

def process_file(file_path, columns_to_keep=None):
    input_path = os.path.join(DATA_DIR, 'raw', file_path)
    file_extension = file_path.split('.')[-1].lower()
    
    if file_extension == 'json':
        with open(input_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        if 'data' in data:
            champions_data = data['data']
            arr = []
            for champions in champions_data :
                arr.append(champions_data[champions])
            df = pd.DataFrame(arr)

            if 'spells' in df.columns:
                spells_df = pd.json_normalize(df['spells'])
                spells_df.columns = [f'spell.{col}' for i, col in enumerate(spells_df.columns)]
                df = df.drop('spells', axis=1)
                df = pd.concat([df, spells_df], axis=1)

                for col in spells_df.columns:
                    if isinstance(spells_df[col].iloc[0], dict):
                        nested_df = pd.json_normalize(spells_df[col])
                        nested_df.columns = [f'{col}.{sub_col}' for sub_col in nested_df.columns]
                        spells_df = spells_df.drop(col, axis=1)
                        spells_df = pd.concat([spells_df, nested_df], axis=1)

                df = pd.concat([df, spells_df], axis=1)

            if 'passive' in df.columns:
                passive_df = pd.json_normalize(df['passive'])
                passive_df.columns = [f'passive.{col}' for col in passive_df.columns]
                df = df.drop('passive', axis=1)
                df = pd.concat([df, passive_df], axis=1)

    elif file_extension == 'csv':
        df = pd.read_csv(input_path, delimiter=';')
    
    if columns_to_keep is not None:
        missing_columns = [col for col in columns_to_keep if col not in df.columns]
        if missing_columns:
            df = df.drop(columns=missing_columns, errors='ignore')
        df = df[columns_to_keep]
    
    file_name = os.path.basename(file_path).split('.')[0] + "Filter.csv"
    output_file_path = os.path.join("data/interim", file_name)
    df.to_csv(output_file_path, index=False, sep=';') 
    
    return df


if __name__ == "__main__":
    json_file_path = "championFull.json"
    csv_file_path = "lolStats.csv"
    
    columns_to_keep_csv = ["Name", "Class", "Role", "Tier", "Win %", "Pick %", "Ban %", "KDA"] 
    columns_to_keep_json = ['name', 'title', 'lore', 'spell.0.id', 'spell.0.name', 'spell.0.description', 'spell.1.id', 'spell.1.name', 'spell.1.description', 'spell.2.id', 'spell.2.name', 'spell.2.description', 'spell.3.id', 'spell.3.name', 'spell.3.description', "passive.name", "passive.description"] 
    
    df_json = process_file(json_file_path, columns_to_keep_json)

    df_csv = process_file(csv_file_path, columns_to_keep_csv)
    