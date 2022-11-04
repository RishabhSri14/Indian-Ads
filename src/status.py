from googleapiclient.discovery import build
import json
import os
import time
from GetData import ExtractData
from PIL import Image
import urllib.request as urll
import random
import imghdr
import shutil
# NUM_PER_KEYWORD=100

#----------------- Get data and upload in spreadsheet---------------------------------------- 
# Download and update the spreadsheet with the content under a particular category and subcategory
def DownloadAndUpdate(path, spread):
    spread.Check_FileStructure(path)
    print("Gathering keywords...")
    list_of_keywords=spread.GetListOfKeywords(path)
    print("Keywords Collected\a")
    print("Extracting data from Keywords...")
    dat=ExtractData(list_of_keywords,10)
    dat.download_image(path)
    print("Data Successfully Collected")
    print("Filling Spreadsheet...")
    for keyword in list_of_keywords:
        spread.AddExample(path,keyword)
    print("Spreadsheet Successfully Updated")

# Download and update the spreadsheet with the content under a particular category and subcategory and for a particular keyword
def DownloadAndUpdate_KeyWord(path, keyword, spread):
    spread.Check_FileStructure(path)
    list_of_keywords=[]
    list_of_keywords.append(keyword+" Indian Ads")
    dat=ExtractData(list_of_keywords,10)
    dat.download_image(path)
    for keyword in list_of_keywords:
        spread.AddExample(path,keyword)

#-------------------------------------------------------------------------------------------------------
#-----------------------Getting data from internet and storing in local storage----------------

# Download data for a particular key-word
def Download_KeyWord(path, keyword, num,api_key_index):
    if not os.path.exists("../Data/"+path):
        print("File Error")
        os.makedirs("../Data/"+path)
    if not os.path.exists("../ImgData/"+path+"/"+keyword):
        print("File Error")
        os.makedirs("../ImgData/"+path+"/"+keyword)   
    list_of_keywords=[]
    list_of_keywords.append(keyword)
    dat=ExtractData(list_of_keywords,num)
    print("Gathering data for {}...".format(keyword))
    k=dat.download_image(path,api_key_index)
    if(k==-1):
        return -1
    print("Data Successfully Collected")

# Getting total number of images for a keyword
def GetNoOfImages(path, Keyword):
    with open('../Data/'+path+"/"+Keyword,) as f:
        data=json.load(f)
    c=0
    for x in data:
        c+=1
    return c

# Getting Status Total data
def GetStatusOfAdsjson():
    with open("Ads.json",) as f:
        data=json.load(f)
    c=0
    for k in data:
        print(k,end=" ")
        n=0
        for l in data[k]:
            c+=1
            n+=1
        print(n)
    print(c)

def GetStatusOfImgData(path, keyword):
    fold="../ImgData/"+path+"/"+keyword
    c=0
    for img in os.listdir(fold):
        c+=1
    return c
    

def GetNumOfDownloadedImages(keyword):
    c=0
    if keyword in os.listdir("../ImgData"):
        
        for images in os.listdir("../ImgData/"+keyword):
            c+=1
    return c

def ConvertWebpToJPG():
    for keyword in os.listdir("../ImgData"):
        print(keyword+"...")
        for images in os.listdir("../ImgData/"+keyword):
            if( images[-4:]=="webp"):
                im=Image.open("../ImgData/"+keyword+"/"+images).convert("RGB")
                im.save("../ImgData/"+keyword+"/"+images[:-4]+"jpg","jpeg")
                os.remove("../ImgData/"+keyword+"/"+images)
        

def CopyFileFromImageToImgData(key):
    for keyword in os.listdir("../Images"):
        if(keyword[:keyword.find("_")]== key):

            if(imghdr.what("../Images/"+keyword)!=None):
                    Dat_filename="../ImgData/"+key+"/"+keyword[:keyword.find(".")+1]+imghdr.what("../Images/"+keyword)
                    shutil.copyfile("../Images/"+keyword,Dat_filename)


    



        
