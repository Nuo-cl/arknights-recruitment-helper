import json
import itertools

def read_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    data_ = {}
    for k,v in data.items():
        data_[frozenset(k.split(' '))] = v
    return data_

def calculate_tag_combination(tag_combination, data, min_rarity):
    # 检查标签组合是否存在于数据中
    if frozenset(tag_combination) not in data:
        return []  # 如果不存在，直接返回空列表

    operators = data[frozenset(tag_combination)]
    if min_rarity == 4:
        for operator in operators:
            if operator[1] < 4:
                return []
            elif operator[1] == 5:
                operators.remove(operator)
    elif min_rarity == 5:
        for operator in operators:
            if operator[1] < 5:
                return []
    
    # 按照稀有度排序
    operators.sort(key=lambda x: x[1], reverse=True)

    return operators

def calculate_selection(tags, path):
    data = read_json(path)
    tags = list(set(tags))
    selection_4 = {}
    selection_5 = {}
    for i in range(1, len(tags)+1):
        # 选取所有i个标签的组合
        tag_combinations = itertools.combinations(tags, i)
        for tag_combination in tag_combinations:
            operators_4 = calculate_tag_combination(tag_combination, data, 4)
            operators_5 = calculate_tag_combination(tag_combination, data, 5)
            if len(operators_4) > 0:
                selection_4[tag_combination] = operators_4
            if len(operators_5) > 0:
                selection_5[tag_combination] = operators_5
    return selection_4, selection_5        

if __name__ == '__main__':
    tags = ['近战位', '减速']
    selection_4, selection_5 = calculate_selection(tags, './data/operators.json')
    if len(selection_4) == 0 and len(selection_5) == 0:
        print('没有符合条件的高稀有度干员')
    for k,v in selection_4.items():
        print(k, v)
    for k,v in selection_5.items():
        print(k, v)