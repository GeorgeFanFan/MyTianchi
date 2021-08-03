import pandas as pd
import csv
import re
import cv2

from PIL import Image, ImageDraw, ImageFont
import numpy as np


# 此函数在bounding box旁边添加中文
def add_chinese(img, name, text_position):
    # 图像从OpenCV格式转换成PIL格式
    img_PIL = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    # 字体
    font = ImageFont.truetype('simhei.ttf', 60, encoding="utf-8")

    # 开始显示
    draw = ImageDraw.Draw(img_PIL)
    draw.text(text_position, name, font=font, fill=(255, 0, 0))

    # 转换回OpenCV格式
    img_OpenCV = cv2.cvtColor(np.asarray(img_PIL), cv2.COLOR_RGB2BGR)

    return img_OpenCV

with open('2train_rname.csv',encoding='utf-8') as f:
    reader = csv.reader(f)
    #print(type(reader))
    #i=1
    for row in reader:
        print(row[4].split('.')[-2])
        #print(row[-1])
        #data = row[-1].split(',')
        re1 = r"\"geometry\":\[(.*?)\],\"type\""
        res1 = re.findall(re1, row[-1])
        re2 = r"\"标签\":\"(.*?)\""
        res2 = re.findall(re2, row[-1])
        #print(res1)
        #print(res2)
        # if "badge" == res2[0]:
        #     print("True")
        img = cv2.imread(row[4])
        if img is None:
            continue
        h = img.shape[0]
        w = img.shape[1]
        if len(res1) != len(res2):
            print("111111111111111111111111111111")
            print("wroooooooooooooooooooooong")
            print("wroooooooooooooooooooooong")
        for i in range(0,len(res2)):
            bbox = res1[i].split(',')
            bb1 = float(bbox[0])
            bb2 = float(bbox[1])
            bb3 = float(bbox[2])
            bb4 = float(bbox[3])
            b = (float(bb1),float(bb2),float(bb3),float(bb4))
            #print(b)
            cv2.rectangle(img, (int(bb1),int(bb2)), (int(bb3), int(bb4)),(0, 255, 0), 2)
            img = add_chinese(img, res2[i], (int(bb1), int(bb2) - 40))

            #print(row[4].split('.')[-2])
        cv2.imwrite(r'C:\Users\FANZhiyu\PycharmProjects\TianChi\draw\%s.jpg'%(row[4].split('.')[-2]), img)
        print("OK")
