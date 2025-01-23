import pandas as pd

file_path = "data/test.csv"  
# df =  pd.read_csv(file_path, sep=";")
output_file = "data/top_results.csv"


class Top:
    def top_win(df, nbr):
        top_Win = df[['Name', 'Win %']].sort_values(by='Win %', ascending=False).head(nbr)
        with open(output_file, mode="w", encoding="utf-8") as f:
            top_Win.to_csv(f, index=False, sep=";", lineterminator="\n")
        print(top_Win)

    def top_pick(df, nbr):
        top_Pick = df[['Name', 'Pick %']].sort_values(by='Pick %', ascending=False).head(nbr)
        with open(output_file, mode="w", encoding="utf-8") as f:
            top_Pick.to_csv(f, index=False, sep=";", lineterminator="\n")
        print(top_Pick)

    def top_ban(df, nbr):
        top_Ban = df[['Name', 'Ban %']].sort_values(by='Ban %', ascending=False).head(nbr)
        with open(output_file, mode="w", encoding="utf-8") as f:
            top_Ban.to_csv(f, index=False, sep=";", lineterminator="\n")
        print(top_Ban)

    def top_kda(df, nbr):
        top_KDA = df[['Name', 'KDA']].sort_values(by='KDA', ascending=False).head(nbr)
        with open(output_file, mode="w", encoding="utf-8") as f:
            top_KDA.to_csv(f, index=False, sep=";", lineterminator="\n")
        print(top_KDA)
