import requests
import time

url = "https://visitor-badge.laobi.icu/badge?page_id=gcarlo11.gcarlo11" # ganti dengan URL target

total_hits = 1000   # berapa kali mau hit
delay = 0.1         # jeda antar hit (detik)

for i in range(total_hits):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Hit {i+1}: Sukses")
        else:
            print(f"Hit {i+1}: Gagal, status {response.status_code}")
    except Exception as e:
        print(f"Hit {i+1}: Error {e}")
    time.sleep(delay)
