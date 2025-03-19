import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
import easyocr
import torch
import time

from helper_tools import calculate_selection

if __name__ == '__main__':
    # 强制使用CPU
    device = torch.device('cpu')
    reader = easyocr.Reader(['ch_sim'], gpu=False)  # 简体中文和英文

    # 识别图片中的文字
    start_time = time.time()
    result = reader.readtext('./img/image.png')
    end_time = time.time()
    print(f"OCR推理时间: {end_time - start_time:.2f}秒")

    tags = []
    # 输出结果
    for (bbox, text, prob) in result:
        if ('干员' in text) and text != '高级资深干员':
            text = text.replace("干员", "")

    selection_4, selection_5 = calculate_selection(tags, './data/operators.json')
    if len(selection_4) == 0 and len(selection_5) == 0:
        print('没有符合条件的高稀有度干员')
    else:
        print('四星选择：')
        print(selection_4)
        print()
        print('五星选择：')
        print(selection_5)