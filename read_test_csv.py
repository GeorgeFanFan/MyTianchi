import csv
import os
import json
import numpy as np

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

def fzy_giou(x0,y0,x1,y1, x2,y2,x3,y3):
    x0 = int(x0)
    y0 = int(y0)
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)
    x3 = int(x3)
    y3 = int(y3)
    iou = fzy_iou(x0,y0,x1,y1, x2,y2,x3,y3)
    w = max(x1, x3) - min(x0, x2)
    h = max(y1, y3) - min(y0, y2)
    C = w*h

    s1 = (x1 - x0) * (y1 - y0)
    s2 = (x3 - x2) * (y3 - y2)
    w = max(0, min(x1, x3) - max(x0, x2))
    h = max(0, min(y1, y3) - max(y0, y2))
    inter = w * h

    giou = iou - (np.abs(C / (s1 + s2 - inter)) / np.abs(C))
    # s1 = (x1 - x0) * (y1 - y0)
    # s2 = (x3 - x2) * (y3 - y2)
    # w = max(0, min(x1, x3) - max(x0, x2))
    # h = max(0, min(y1, y3) - max(y0, y2))
    # inter = w * h
    # iou = inter / (s1 + s2 - inter)
    return giou

label_file = r"C:\Users\FANZhiyu\PycharmProjects\TianChi\labels"

list=[]
with open('2_testb_imageid.csv',encoding='utf-8') as f:
    reader = csv.reader(f)
    #print(type(reader))
    #i=1

    for row in reader:
        image_name = row[1].split('/')[-1]
        #print(row[1].split('/')[-1])
        list.append(image_name.split(".")[0])
        #break

#print(list)
res = []
for root, dirs, files in os.walk(label_file):
    for file in files:
        #print(file)
        name = file.split(".")[0]
        image_id = list.index(name)-1
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
                            if iou > 0.01 :
                                #print(file.split())
                                x1 = int(i.split(' ')[1])
                                y1 = int(i.split(' ')[2])
                                x2 = int(i.split(' ')[3])
                                y2 = int(i.split(' ')[4])
                                cur_conf = float(conf)
                                cur_res = {"image_id": image_id,"category_id":1,"bbox":[x1, y1, x2, y2],"score":cur_conf}
                                #print(cur_res)
                                res.append(cur_res)
                                flag = True
                        if label2 == "2":
                            iou = fzy_iou(i.split(' ')[1], i.split(' ')[2], i.split(' ')[3], i.split(' ')[4],
                                            j.split(' ')[1], j.split(' ')[2], j.split(' ')[3], j.split(' ')[4])
                            #print(iou)
                            if iou > 0.3 :
                                #print(file.split())
                                x1 = int(i.split(' ')[1])
                                y1 = int(i.split(' ')[2])
                                x2 = int(i.split(' ')[3])
                                y2 = int(i.split(' ')[4])
                                cur_conf = float(conf)
                                cur_res = {"image_id": image_id,"category_id":2,"bbox":[x1, y1, x2, y2],"score":cur_conf}
                                #print(cur_res)
                                res.append(cur_res)
                                flag = True
                        if label2 == "3":
                            iou = fzy_iou(i.split(' ')[1], i.split(' ')[2], i.split(' ')[3], i.split(' ')[4],
                                            j.split(' ')[1], j.split(' ')[2], j.split(' ')[3], j.split(' ')[4])
                            #print(iou)
                            if iou > 0.3:
                                #print(file.split())
                                x1 = int(i.split(' ')[1])
                                y1 = int(i.split(' ')[2])
                                x2 = int(i.split(' ')[3])
                                y2 = int(i.split(' ')[4])
                                cur_conf = float(conf)
                                cur_res = {"image_id": image_id,"category_id":3,"bbox":[x1, y1, x2, y2],"score":cur_conf}
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
                        # print(cur_res)
                        res.append(cur_res)



#final_res = json.dumps(res)
filename = "fzy_last.json"
with open(filename,'w') as file_obj:
    json.dump(res,file_obj)