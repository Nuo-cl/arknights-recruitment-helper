from bs4 import BeautifulSoup
import json

def read_txt():
    with open('./data/prts.txt', 'r', encoding='utf-8') as f:
        html = f.read()
    return html

def get_operator(html):
    soup = BeautifulSoup(html, 'html.parser')
    # 查找所有<div class="flex flex-wrap items-center justify-center" data-v-30767bcb="">
    divs = soup.find_all('div', class_='flex flex-wrap items-center justify-center')

    # 新建空字典
    operator = {}
    # 遍历tag_div
    for div in divs:
        # 获取div的父标签的父标签
        parent = div.parent.parent
        
        operators = {}
        tags = [d.text for d in div.find_all('div', class_='tag')]

        operator_rarity = []
        # 获取这个标签内的所有class是avatar-container的div
        avatars = parent.find_all('div', class_='avatar-container')
        for avatar in avatars:
            aref = avatar.find('a')
            # 获取a标签的href属性
            name = aref['href'].split('/')[-1]

            rarity_div = avatar.find('div', class_='rarity').find('img')
            rarity = int(rarity_div['src'].split('.')[-2].split('_')[-1]) + 1
            operator_rarity.append([name, rarity])

        operator[' '.join(tags)] = operator_rarity
    return operator

def output(operator):
    # 存储到json文件
    with open('./data/operators.json', 'w', encoding='utf-8') as f:
        json.dump(operator, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    html = read_txt()
    operator = get_operator(html)
    output(operator)