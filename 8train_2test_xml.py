# import os
# import numpy as np
# import shutil
#
# file = r"C:\Users\FANZhiyu\Desktop\Caltech Pedestrain Dataset\Caltech_Pedestrian_Detection_Benchmark\data\after transform\JPEGImage_5frame"
# file2 = r"C:\Users\FANZhiyu\Desktop\Caltech Pedestrain Dataset\Caltech_Pedestrian_Detection_Benchmark\data\after transform"
#
# #构建所有文件名的列表，dir为label
# filename = []
# #label = []
# for root, dirs, files in os.walk(file):
#     for f in files:
#         #print(os.path.join(root,f))
#         filename.append(os.path.join(root,f))
#
# #打乱文件名列表
# #print(filename)
# np.random.shuffle(filename)
# #划分训练集、测试集，默认比例8:2
# train = filename[:int(len(filename)*0.8)]
# #print(train)
# test = filename[int(len(filename)*0.8):]
# #print(test)
#
# label_path = r"C:\Users\FANZhiyu\Desktop\Caltech Pedestrain Dataset\Caltech_Pedestrian_Detection_Benchmark\data\after transform\labels_yolov5_5frame"
# #分别写入train.txt, test.txt
# with open(os.path.join(file2,'train.txt'), 'w') as f1, open(os.path.join(file2,'test.txt'), 'w') as f2:
#     for i in train:
#         f1.write(i + '\n')
#
#         train_new_path = r"C:\Users\FANZhiyu\Desktop\Caltech Pedestrain Dataset\Caltech_Pedestrian_Detection_Benchmark\data\after transform\8_2\JPEGImage_5frame_train"
#         #print(i.split('\\')[-1].split(".")[0]+".txt")
#         shutil.copy(i, os.path.join(train_new_path,i.split('\\')[-1]))
#
#         train_label_path = r"C:\Users\FANZhiyu\Desktop\Caltech Pedestrain Dataset\Caltech_Pedestrian_Detection_Benchmark\data\after transform\8_2\labels_yolov5_5frame_train"
#         shutil.copy(os.path.join(label_path, i.split('\\')[-1].split(".")[0]+".txt"), os.path.join(train_label_path, i.split('\\')[-1].split(".")[0]+".txt"))
#
#
#     for j in test:
#         f2.write(j + '\n')
#
#         test_new_path = r"C:\Users\FANZhiyu\Desktop\Caltech Pedestrain Dataset\Caltech_Pedestrian_Detection_Benchmark\data\after transform\8_2\JPEGImage_5frame_test"
#         shutil.copy(j, os.path.join(test_new_path, j.split('\\')[-1]))
#
#         test_label_path = r"C:\Users\FANZhiyu\Desktop\Caltech Pedestrain Dataset\Caltech_Pedestrian_Detection_Benchmark\data\after transform\8_2\labels_yolov5_5frame_test"
#         shutil.copy(os.path.join(label_path, j.split('\\')[-1].split(".")[0]+".txt"), os.path.join(test_label_path, j.split('\\')[-1].split(".")[0]+".txt"))
#
#
# print('成功！')

import os
import numpy as np
import shutil

file = r"C:\Users\FANZhiyu\PycharmProjects\TianChi\2_images"  # 原始图片所在文件夹

# 构建所有文件名的列表，dir为label
filename = []
# label = []
for root, dirs, files in os.walk(file):
    for f in files:
        # print(os.path.join(root,f))
        filename.append(os.path.join(root, f))

# 打乱文件名列表
# print(filename)
np.random.shuffle(filename)
# 划分训练集、测试集，默认比例8:2
train = filename[:int(len(filename) * 0.8)]
# print(train)
test = filename[int(len(filename) * 0.8):]
# print(test)

label_path = r"C:\Users\FANZhiyu\PycharmProjects\TianChi\labels"
for i in train:
    # f1.write(i + '\n')
    train_new_path = r"C:\Users\FANZhiyu\PycharmProjects\TianChi\8_2\images\train2017"
    # f1.write(os.path.join(train_new_path,i.split('/')[-1]) + '\n')

    # print(i.split('\\')[-1].split(".")[0]+".txt")
    #shutil.copy(i, os.path.join(train_new_path, i.split('\\')[-1]))

    train_label_path = r"C:\Users\FANZhiyu\PycharmProjects\TianChi\8_2\labels\train2017"
    # shutil.copy(os.path.join(label_path, i.split('\\')[-1].split(".")[0] + ".txt"),
    #             os.path.join(train_label_path, i.split('\\')[-1].split(".")[0] + ".txt"))
    with open("train.txt", "a") as f:
        f.write( i.split('\\')[-1].split(".")[0] + '\n')

for j in test:
    # f2.write(j + '\n')
    test_new_path = r"C:\Users\FANZhiyu\PycharmProjects\TianChi\8_2\images\val2017"
    # f2.write(os.path.join(test_new_path, j.split('/')[-1]) + '\n')

    # shutil.copy(j, os.path.join(test_new_path, j.split('\\')[-1]))

    test_label_path = r"C:\Users\FANZhiyu\PycharmProjects\TianChi\8_2\labels\val2017"
    # shutil.copy(os.path.join(label_path, j.split('\\')[-1].split(".")[0] + ".txt"),
    #             os.path.join(test_label_path, j.split('\\')[-1].split(".")[0] + ".txt"))
    with open("test.txt", "a") as f:
        f.write( j.split('\\')[-1].split(".")[0] + '\n')

print('成功！')

