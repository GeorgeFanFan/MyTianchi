import csv
import os
import json
import numpy as np

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

def fzy_iou(x0,y0,x1,y1, x2,y2,x3,y3):
    x0 = int(x0)
    y0 = int(y0)
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)
    x3 = int(x3)
    y3 = int(y3)
    s1 = (x1 - x0) * (y1 - y0)
    s2 = (x3 - x2) * (y3 - y2)
    w = max(0, min(x1, x3) - max(x0, x2))
    h = max(0, min(y1, y3) - max(y0, y2))
    inter = w * h
    iou = inter / (s1 + s2 - inter)
    return iou

label_file = r"C:\Users\FANZhiyu\PycharmProjects\TianChi\results"

list=[]
image_list = []
with open('2_testa_user.csv',encoding='utf-8') as f:
    reader = csv.reader(f)
    #print(type(reader))
    #i=1

    for row in reader:
        image_name = row[0].split('/')[-1]
        # print(row[0].split('/')[-1])
        list.append(image_name.split(".")[0])
        image_list.append(image_name)
        #break

#print(list)
res = []
for root, dirs, files in os.walk(label_file):
    for file in files:
        #print(file)
        name = file.split(".")[0]
        image_id = list.index(name)
        img = cv2.imread("2_test_imagesa\%s"%(image_list[image_id]))
        with open(root+"\\"+file,encoding='utf-8') as f:
            #x = f.readlines()
            tmp = f.readlines()
            for i in tmp:
                i = i[:-1] # 去除换行符
                #print(i)
                #print(i.split(' ')[0]) # label
                #print(i.split(' ')[-1]) # confidence
                label = i.split(' ')[0]
                conf = i.split(' ')[-1]
                if label == "1":
                    flag = False
                    for j in tmp:
                        #print("1111111111111111111111111")
                        #print(j)
                        label2 = j.split(' ')[0]
                        #print(label2)
                        if label2 == "0":
                            iou = fzy_iou(i.split(' ')[1], i.split(' ')[2], i.split(' ')[3], i.split(' ')[4],
                                            j.split(' ')[1], j.split(' ')[2], j.split(' ')[3], j.split(' ')[4])
                            #print(iou)
                            if iou != 0 :
                                #print(file.split())
                                x1 = int(i.split(' ')[1])
                                y1 = int(i.split(' ')[2])
                                x2 = int(i.split(' ')[3])
                                y2 = int(i.split(' ')[4])
                                cur_conf = float(conf)
                                cur_res = {"image_id": image_id,"category_id":1,"bbox":[x1, y1, x2, y2],"score":cur_conf}
                                #print(cur_res)
                                res.append(cur_res)
                                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                                img = add_chinese(img, "guarder", (x1, y1))
                                flag = True
                        if label2 == "2":
                            iou = fzy_iou(i.split(' ')[1], i.split(' ')[2], i.split(' ')[3], i.split(' ')[4],
                                            j.split(' ')[1], j.split(' ')[2], j.split(' ')[3], j.split(' ')[4])
                            #print(iou)
                            if iou >0.4 :
                                #print(file.split())
                                x1 = int(i.split(' ')[1])
                                y1 = int(i.split(' ')[2])
                                x2 = int(i.split(' ')[3])
                                y2 = int(i.split(' ')[4])
                                cur_conf = float(conf)
                                cur_res = {"image_id": image_id,"category_id":2,"bbox":[x1, y1, x2, y2],"score":cur_conf}
                                #print(cur_res)
                                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                                img = add_chinese(img, "rightdressed", (x1, y1))
                                res.append(cur_res)
                                flag = True
                        if label2 == "3":
                            iou = fzy_iou(i.split(' ')[1], i.split(' ')[2], i.split(' ')[3], i.split(' ')[4],
                                            j.split(' ')[1], j.split(' ')[2], j.split(' ')[3], j.split(' ')[4])
                            #print(iou)
                            if iou >0.4:
                                #print(file.split())
                                x1 = int(i.split(' ')[1])
                                y1 = int(i.split(' ')[2])
                                x2 = int(i.split(' ')[3])
                                y2 = int(i.split(' ')[4])
                                cur_conf = float(conf)
                                cur_res = {"image_id": image_id,"category_id":3,"bbox":[x1, y1, x2, y2],"score":cur_conf}
                                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                                img = add_chinese(img, "wrongdressed", (x1, y1))
                                #print(cur_res)
                                res.append(cur_res)
                                flag = True
                    if flag == False:
                        x1 = int(i.split(' ')[1])
                        y1 = int(i.split(' ')[2])
                        x2 = int(i.split(' ')[3])
                        y2 = int(i.split(' ')[4])
                        cur_conf = float(conf)
                        cur_res = {"image_id": image_id, "category_id": 3, "bbox": [x1, y1, x2, y2], "score": cur_conf}
                        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                        img = add_chinese(img, "wrongdressed", (x1, y1))
                        # print(cur_res)
                        res.append(cur_res)
        cv2.imwrite(r'C:\Users\FANZhiyu\PycharmProjects\TianChi\results_draw\%s' % (image_list[image_id]), img)
        print("OK")



#final_res = json.dumps(res)
filename = "fzy_res.json"
with open(filename,'w') as file_obj:
    json.dump(res,file_obj)