# -*- coding:utf-8 -*-

import os
from lxml import etree, objectify
import csv
import re
import cv2

#vbb_inputdir = r"C:\Users\FANZhiyu\Desktop\Caltech Pedestrain Dataset\Caltech_Pedestrian_Detection_Benchmark\data\annotations"
vbb_outdir = r"tianchi_XML"
with open('2train_rname.csv',encoding='utf-8') as f:
    reader = csv.reader(f)
    #print(type(reader))
    #i=1
    for row in reader:
        print(row[4].split('.')[-2])
        if row[4].split('.')[-2] == "2_images/4b517d6e_d654_47de_ae15_5bc214940785":
            continue
        if row[4].split('.')[-2] == "2_images/bf3a1936_6b0b_4ace_b0bd_e37a4d897393":
            continue
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

        bbox_type = 'xyxy'
        E = objectify.ElementMaker(annotate=False)
        anno_tree = E.annotation(
            E.folder('tianchi_XML'),
            E.filename(row[4].split('.')[-2]),
            E.source(
                E.database('TianChi'),
                E.annotation('TianChi'),
                E.image('TianChi'),
                E.url('None')
            ),
            E.size(
                E.width(img.shape[1]),
                E.height(img.shape[0]),
                E.depth(3)
            ),
            E.segmented(0),
        )

        for i in range(0, len(res2)):
            bbox = res1[i].split(',')
            bb1 = int(float(bbox[0]))
            bb2 = int(float(bbox[1]))
            bb3 = int(float(bbox[2]))
            bb4 = int(float(bbox[3]))
            if bb2 > w:
                bb2 = w
            if bb4 > h:
                bb4 = h
            b = (float(bb1),float(bb2),float(bb3),float(bb4))
            print(b)
            if res2[i] == "badge":
                cls_id = 0
            elif res2[i] == "person":
                cls_id = 1
            elif res2[i] == "clothes":
                cls_id = 2
            elif res2[i] == "wrongclothes":
                cls_id = 3

            E = objectify.ElementMaker(annotate=False)
            anno_tree.append(
                E.object(
                    E.name(res2[i]),
                    E.bndbox(
                        E.xmin(bb1),
                        E.ymin(bb2),
                        E.xmax(bb3),
                        E.ymax(bb4)
                    ),
                    E.difficult(0)
                        # E.occlusion(anno["occlusion"][index])
                )
            )
            outfile = os.path.join(vbb_outdir, row[4].split('.')[-2] + ".xml")
            print("Generating annotation xml file of picture: ", row[4].split('.')[-2])
            # 生成最终的xml文件，对应一张图片
            etree.ElementTree(anno_tree).write(outfile, pretty_print=True)

