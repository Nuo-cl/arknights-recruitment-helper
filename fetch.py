import requests
from bs4 import BeautifulSoup

def fetch():
    with open('./data/prts.txt', 'r', encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup

# 把解析后的html按格式输出到prts_refined.txt文件中
def output():
    soup = fetch()
    with open('./data/prts_refined.txt', 'w', encoding='utf-8') as f:
        f.write(soup.prettify())

if __name__ == '__main__':
    output()