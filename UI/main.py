import requests
import pandas as pd

url = 'https://openapi-h8a3.onrender.com/pico_w/?count=7'

r = requests.get(url=url)

if r.status_code == 200:
    print('下載成功')
    data = r.json()

dataFrame = pd.DataFrame(data)
print(dataFrame)