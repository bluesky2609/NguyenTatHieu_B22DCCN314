import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

df = pd.read_csv('result.csv')

columns_to_exclude = ['player', 'age', 'nationality', 'team', 'position']
stat_columns = [col for col in df.columns if col not in columns_to_exclude]

max_histograms = 20
selected_columns = stat_columns[:max_histograms]

os.makedirs('histograms', exist_ok=True)

for stat in selected_columns:
    plt.figure(figsize=(8, 6))
    sns.histplot(df[stat].dropna(), kde=True, bins=30)
    plt.title(f'Histogram of {stat}')
    plt.xlabel(stat)
    plt.ylabel('Frequency')
    plt.savefig(f'histograms/{stat}_histogram.png')
    plt.close()

print("Histograms have been saved in the 'histograms' folder for the selected 20 attributes.")
