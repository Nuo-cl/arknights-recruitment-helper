import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
# 屏蔽EasyOCR的日志警告
import logging
logging.getLogger('easyocr').setLevel(logging.ERROR)

import easyocr
import torch
import time

from helper_tools import calculate_selection

DATA_PATH = './data/operators.json'
IMG_PATH = './img/image.png'

if __name__ == '__main__':
    # 记录程序开始时间
    program_start_time = time.time()
    
    # 强制使用CPU
    device = torch.device('cpu')
    reader = easyocr.Reader(['ch_sim'], gpu=False)  # 简体中文和英文

    # 识别图片中的文字
    start_time = time.time()
    result = reader.readtext(IMG_PATH)
    end_time = time.time()
    print(f"OCR推理时间: {end_time - start_time:.2f}秒")

    tags = []
    # 输出结果
    for (bbox, text, prob) in result:
        if ('干员' in text) and text != '高级资深干员':
            text = text.replace("干员", "")
        tags.append(text)

    selection_4, selection_5 = calculate_selection(tags, DATA_PATH)
    if len(selection_4) == 0 and len(selection_5) == 0:
        print('没有符合条件的高稀有度干员')
    else:
        if len(selection_4) > 0:
            print('4星干员:')
            for k, v in selection_4.items():
                print(k, v)
        if len(selection_5) > 0:
            print('5星干员:')
            for k, v in selection_5.items():
                print(k, v)
    
    # 计算并打印程序总运行时间
    program_end_time = time.time()
    print(f"程序总运行时间: {program_end_time - program_start_time:.2f}秒")
                