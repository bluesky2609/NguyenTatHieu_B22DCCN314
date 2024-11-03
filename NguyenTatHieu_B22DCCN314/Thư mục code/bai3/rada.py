import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import pi
import argparse

def radar_chart(player1, player2, attributes, data):
    p1_data = data[data['name'] == player1][attributes].values.flatten()
    p2_data = data[data['name'] == player2][attributes].values.flatten()
    
    if p1_data.size == 0 or p2_data.size == 0:
        print("Lỗi: Không tìm thấy cầu thủ hoặc chỉ số không hợp lệ.")
        return

    num_vars = len(attributes)
    angles = [n / float(num_vars) * 2 * pi for n in range(num_vars)]
    angles += angles[:1]  

    p1_data = np.append(p1_data, p1_data[0])
    p2_data = np.append(p2_data, p2_data[0])

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    plt.xticks(angles[:-1], attributes, color='grey', size=8)
    ax.plot(angles, p1_data, linewidth=1, linestyle='solid', label=player1)
    ax.fill(angles, p1_data, 'b', alpha=0.1)

    ax.plot(angles, p2_data, linewidth=1, linestyle='solid', label=player2)
    ax.fill(angles, p2_data, 'r', alpha=0.1)

    plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
    plt.title(f"So sánh {player1} và {player2}")
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Vẽ biểu đồ radar so sánh cầu thủ.")
    parser.add_argument("--p1", type=str, required=True, help="Tên cầu thủ thứ nhất")
    parser.add_argument("--p2", type=str, required=True, help="Tên cầu thủ thứ hai")
    parser.add_argument("--Attribute", type=str, required=True, help="Danh sách các chỉ số, cách nhau bởi dấu phẩy")

    args = parser.parse_args()
    
    data = pd.read_csv("results2.csv")

    attributes = args.Attribute.split(",")

    radar_chart(args.p1, args.p2, attributes, data)
