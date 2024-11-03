import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('result.csv')

attributes = data.select_dtypes(include=[float, int])

attributes = attributes.fillna(attributes.mean())

scaler = StandardScaler()
scaled_data = scaler.fit_transform(attributes)

inertia = []
K = range(1, 11)
for k in K:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_data)
    inertia.append(kmeans.inertia_)

plt.figure(figsize=(8, 5))
plt.plot(K, inertia, 'bx-')
plt.xlabel('Số cụm (k)')
plt.ylabel('Inertia')
plt.title('Phương pháp Elbow để xác định số cụm tối ưu')
plt.show()

k = 4
kmeans = KMeans(n_clusters=k, random_state=42)
clusters = kmeans.fit_predict(scaled_data)

data['Cluster'] = clusters

cluster_means = data.groupby('Cluster').mean()

print("Trung bình các chỉ số của từng cụm:")
print(cluster_means)

plt.figure(figsize=(10, 6))
sns.scatterplot(x=scaled_data[:, 0], y=scaled_data[:, 1], hue=clusters, palette='viridis', s=100)
plt.xlabel('Chỉ số 1 (chuẩn hóa)')
plt.ylabel('Chỉ số 2 (chuẩn hóa)')
plt.title('Phân cụm các cầu thủ bằng K-means')
plt.legend(title='Cụm')
plt.show()

data.to_csv('clustered_players.csv', index=False)
