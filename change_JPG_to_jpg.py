import os
import shutil

file = r"C:\Users\FANZhiyu\PycharmProjects\TianChi\data\VOCdevkit\VOC2007\JPEGImages"
fileNew = r"C:\Users\FANZhiyu\PycharmProjects\TianChi\data\VOCdevkit\VOC2007\New"
for root, dirs, files in os.walk(file):
    for f in files:
        f_name = f.split('.')[0]
        print(f_name)
        shutil.copy(os.path.join(file, f), os.path.join(fileNew, f_name + ".jpg"))