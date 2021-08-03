import pandas as pd
import csv
import re
import cv2

def convert(size, box):
    dw = 1. / (size[0])
    dh = 1. / (size[1])
    x = (box[0] + box[2]) / 2.0 *dw
    y = (box[1] + box[3]) / 2.0 *dh
    w = (box[2] - box[0])*dw
    h = (box[3] - box[1])*dh
    return x, y, w, h

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
        print(res1)
        print(res2)
        # if "badge" == res2[0]:
        #     print("True")
        img = cv2.imread(row[4])
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
            if bb2 > w:
                bb2 = w
            if bb4 > h:
                bb4 = h
            b = (float(bb1),float(bb2),float(bb3),float(bb4))
            print(b)
            bb = convert((w, h), b)
            if res2[i] == "badge":
                cls_id = 0
            elif res2[i] == "person":
                cls_id = 1
            elif res2[i] == "clothes":
                cls_id = 2
            elif res2[i] == "wrongclothes":
                cls_id = 3
            with open("data/%s.txt"%(row[4].split('.')[-2]), "a") as f:
                f.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
