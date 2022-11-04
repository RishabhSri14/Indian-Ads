from imagededup.methods import CNN
from imagededup.utils import plot_duplicates
import pandas as pd
import matplotlib.pyplot as plt
import json
import os
import time
from PIL import Image
import requests
import cv2
import pickle
plt.rcParams['figure.figsize'] = (15, 10)
def GetNoOfImages(path, Keyword):
    with open('../data/'+path+"/"+Keyword,) as f:
        data=json.load(f)
    c=0
    for x in data:
        c+=1
    return c

def FindDuplicates(startwith):
    cnn =CNN()
    c=0
    # plot_duplicates(image_dir="./temp",duplicate_map=duplicates, filename='cascoon.png')
    for keyword in os.listdir("../ImgData"):
        c+=1
        print(c,keyword)
        if(c<startwith):
            continue
        print("Finding duplicates in "+keyword+" ..." )
        encodings = cnn.encode_images(image_dir="../Data_img/"+keyword)
        # print(encodings)
        duplicates = cnn.find_duplicates(encoding_map=encodings, scores = True)
        # print(duplicates)
        with open(f'../Data_img/{keyword}/Duplicates',"wb") as f:
            pickle.dump(duplicates,f)
        
        for key, value in duplicates.items():
            if len(value) > 0:
                print(key + ",")

def FindDuplicatesKeyword(keyword):
    cnn =CNN()
    # plot_duplicates(image_dir="./temp",duplicate_map=duplicates, filename='cascoon.png')
    if keyword in os.listdir("../Data_img"):
        print("Finding duplicates in "+keyword+" ..." )
        encodings = cnn.encode_images(image_dir="../Data_img/"+keyword)
        # print(encodings)
        duplicates = cnn.find_duplicates(encoding_map=encodings, scores = True)
        # print(duplicates)
        with open(f'../Data_img/{keyword}/Duplicates',"wb+") as f:
            pickle.dump(duplicates,f)
        
        for key, value in duplicates.items():
            if len(value) > 0:
                print(key + ",")

def ShowDuplicates(keyword):
    with open("../Data_img/"+keyword+"/Duplicates","rb") as f:
        data=pickle.load(f)
    checked_img=[]
    copy_batch=[]
    # print(data)
    for img in data:
        # print(img)
        if img in checked_img:
            continue
        checked_img.append(img)
        temp=[]
        temp.append(img)
        for copy in data[img]:
            if copy[0] in checked_img:
                continue
            checked_img.append(copy[0])
            temp.append(copy[0])
        copy_batch.append(temp)
    dup=0
    for lis in copy_batch:
        c=0
        print('{')
        for img in lis:
            c+=1
            print(img)
        print("}")
        dup+=c
    print("Duplicate count= "+ str(dup))




FindDuplicatesKeyword('"Boost" nutrition drink, Indian Ads')
# ShowDuplicates("5 Star Indian Ads")
# FindDuplicates(51)
