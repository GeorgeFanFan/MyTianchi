# 原始数据
2train_rname.csv
2_testa_user.csv
2_testb_imageid.csv
./2_images

# EDA
draw label: python EDA.py
change_JPG_to_jpg.py

# 提取数据label
for yolov5: python read_csv.py
for mmdetection(voc label): python read_csv_xml.py

# data， 去百度网盘上找
for yolov5: python 8train_2test.py
./tianchi
for mmdetection: 8train_2test_xml.py
./data

# read result to json:
python read_test_csv.py

