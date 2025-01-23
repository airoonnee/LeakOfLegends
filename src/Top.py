import pandas as pd

file_path = "data/test.csv"  
df =  pd.read_csv(file_path, sep=";")
output_file = "data/top_results.csv"


top_Win = df[['Name', 'Win %']].sort_values(by='Win %', ascending=False).head(10)
with open(output_file, mode="w", encoding="utf-8") as f:
    top_Win.to_csv(f, index=False, sep=";", lineterminator="\n")
print(top_Win)

output_file = "data/top_results2.csv"

top_Pick = df[['Name', 'Pick %']].sort_values(by='Pick %', ascending=False).head(10)
with open(output_file, mode="w", encoding="utf-8") as f:
    top_Pick.to_csv(f, index=False, sep=";", lineterminator="\n")
print(top_Pick)

output_file = "data/top_results3.csv"

top_Ban = df[['Name', 'Ban %']].sort_values(by='Ban %', ascending=False).head(10)
with open(output_file, mode="w", encoding="utf-8") as f:
    top_Ban.to_csv(f, index=False, sep=";", lineterminator="\n")
print(top_Ban)

output_file = "data/top_results4.csv"

top_KDA = df[['Name', 'KDA']].sort_values(by='KDA', ascending=False).head(10)
with open(output_file, mode="w", encoding="utf-8") as f:
    top_KDA.to_csv(f, index=False, sep=";", lineterminator="\n")
print(top_KDA)
