import pandas as pd

df = pd.read_csv('result.csv')

columns_to_exclude = ['player', 'age', 'nationality', 'team', 'position']
stat_columns = [col for col in df.columns if col not in columns_to_exclude]

team_stats = df.groupby('team')[stat_columns].mean()

best_team_per_stat = team_stats.idxmax()

top_team_counts = best_team_per_stat.value_counts()

print("Đội có điểm cao nhất ở mỗi chỉ số:")
print(best_team_per_stat)

print("\nĐội có phong độ tốt nhất giải:")
print(top_team_counts.head(1))
