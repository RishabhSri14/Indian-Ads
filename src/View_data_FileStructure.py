import json
import os



import time
import status as stat
from PIL import Image
import requests
import urllib.request as urll
import random
import cv2
from matplotlib import pyplot as plt

def showImage(path, keyword):
    if os.path.exists("../ImgData/"+path):
        file="../ImgData/"+path+"/"+keyword
        with open(file,) as f:
            n= stat.GetNoOfImages(path, keyword)
            dat=json.load(f)
            fig = plt.figure(figsize=(10, 7))
  
            rows = 2
            columns = 2
  

            for i in range(4):
                k=random.randint(0,n-1)
                print(i+1,dat[k]['Image'])
                try:
                    urll.urlretrieve(dat[k]['Image'],"temp.jpg")
                    
                except Exception as e:
                    print(e)
                    continue
                Img=cv2.imread("temp.jpg")
                # img = Image.open(resp.text)
                # img.show()
                fig.add_subplot(rows, columns, i+1)
  
                # showing image
                plt.imshow(Img)
                plt.axis('off')
                plt.title("Image_"+str(i+1))
            plt.show()

directory = "../Data"
path=''
c=0
dic={}

for category in os.listdir(directory):
    path+=category+"/"
    print()
    print(category)
    print()
    
    for subcategory in os.listdir(os.path.join(directory,category)):
        print()
        print(subcategory)
        print()
        k=0
        currpath=path+subcategory
        for keyword in os.listdir(directory+'/'+currpath):
            dic[c]=[currpath,keyword]
            print(c,keyword,"Image Data:", stat.GetStatusOfImgData(currpath,keyword[:-5]))
            if(os.path.getsize("../Data/"+currpath+"/"+keyword)!=0):
                print(c,keyword,"Json Data:", stat.GetNoOfImages(currpath,keyword))
            else:
                print(c,keyword,"Json Data:", 0)
            c+=1
            k+=1
        print(f'Keyword Count: {k}')


    path=''
print("Total number of Keyword:", c)
while(1):
    k=(int)(input("Enter the number of the keyword corressponding to which u want to see random data or -1 to exit: ")) 
    if(k==-1):
        break
    else:
        showImage(dic[k][0],dic[k][1])
