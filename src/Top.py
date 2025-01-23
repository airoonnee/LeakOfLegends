import pandas as pd

file_path = "data/test.csv"  
# df =  pd.read_csv(file_path, sep=";")
output_file = "data/top_results.csv"


class Top:
    def top(df, nbr, genre):
        top_Win = df[['Name', genre]].sort_values(by=genre, ascending=False).head(nbr)
        with open(output_file, mode="w", encoding="utf-8") as f:
            top_Win.to_csv(f, index=False, sep=";", lineterminator="\n")
        print(top_Win)
