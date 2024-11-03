import pandas as pd

df = pd.read_csv('result.csv')

columns_to_exclude = ['player', 'age', 'nationality', 'team', 'position']
stat_columns = [col for col in df.columns if col not in columns_to_exclude]

top_players = {
    "stat": [],
    "top_3_highest": [],
    "top_3_lowest": []
}

for stat in stat_columns:
    df[stat] = pd.to_numeric(df[stat], errors='coerce')

    top_3_high = df[['player', stat]].nlargest(3, stat).reset_index(drop=True)
    top_3_high_list = [f"{row['player']} ({row[stat]})" for _, row in top_3_high.iterrows()]

    top_3_low = df[['player', stat]].nsmallest(3, stat).reset_index(drop=True)
    top_3_low_list = [f"{row['player']} ({row[stat]})" for _, row in top_3_low.iterrows()]

    top_players["stat"].append(stat)
    top_players["top_3_highest"].append(", ".join(top_3_high_list))
    top_players["top_3_lowest"].append(", ".join(top_3_low_list))

result_df = pd.DataFrame(top_players)
result_df.to_csv('top_players_stats.csv', index=False)
print("Top 3 cầu thủ có điểm cao nhất và thấp nhất cho mỗi chỉ số đã được lưu vào 'top_players_stats.csv'.")
