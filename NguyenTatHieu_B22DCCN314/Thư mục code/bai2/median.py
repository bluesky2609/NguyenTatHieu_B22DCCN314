import pandas as pd

df = pd.read_csv('result.csv')

columns_to_exclude = ['player', 'age', 'nationality', 'team', 'position']
stat_columns = [col for col in df.columns if col not in columns_to_exclude]

results = []

overall_stats = ['all']
for stat in stat_columns:
    median_val = df[stat].median()
    mean_val = df[stat].mean()
    std_val = df[stat].std()
    overall_stats.extend([median_val, mean_val, std_val])

results.append(overall_stats)

for team in df['team'].unique():
    team_stats = [team]
    team_data = df[df['team'] == team]
    
    for stat in stat_columns:
        median_val = team_data[stat].median()
        mean_val = team_data[stat].mean()
        std_val = team_data[stat].std()
        team_stats.extend([median_val, mean_val, std_val])
    
    results.append(team_stats)

columns = ['team']
for stat in stat_columns:
    columns.extend([f"Median of {stat}", f"Mean of {stat}", f"Std of {stat}"])

results_df = pd.DataFrame(results, columns=columns)
results_df.to_csv('results2.csv', index=False)

print("Kết quả đã được lưu vào 'results2.csv'.")
