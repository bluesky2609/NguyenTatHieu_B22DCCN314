import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.footballtransfers.com"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    transfer_values = soup.find_all('span', class_='player-tag')
    
    with open('transfer_values.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Cầu thủ', 'Giá chuyển nhượng'])  

        for idx, value in enumerate(transfer_values, start=1):
            transfer_value = value.text.strip()  
            writer.writerow([f'Cầu thủ {idx}', transfer_value]) 

    print("Đã ghi giá chuyển nhượng vào tệp 'transfer_values.csv'.")

else:
    print(f"Không thể truy cập trang web. Mã trạng thái: {response.status_code}")
