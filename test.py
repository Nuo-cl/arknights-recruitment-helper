from bs4 import BeautifulSoup
import json
import requests

# 从https://prts.wiki/w/%E5%85%AC%E6%8B%9B%E8%AE%A1%E7%AE%97?filter=2Vd1CEUp7ZRwxVdBRUJKDo9y8vZGEBcue8sE7WoXc93bt9cHy4ZznS获取内容
url = "https://prts.wiki/w/%E5%85%AC%E6%8B%9B%E8%AE%A1%E7%AE%97?filter=2Vd1CEUp7ZRwxVdBRUJKDo9y8vZGEBcue8sE7WoXc93bt9cHy4ZznS"
response = requests.get(url)

if response.status_code == 200:
    html_content = response.text
    print("HTML content fetched successfully.")
    print(html_content)  
else:
    print(f"Failed to fetch HTML content. Status code: {response.status_code}")
