import json
import os
import time
import status as stat
KeywordKey_StartIndex=280
MAX_API_KEYS=48
NUM_PER_KEYWORD=int(input("Enter number of image you want to download per keyword: "))
# Downloading data for all the keyword available 
def CollectData(startwith):
    directory = "../Data"
    path=''
    current_key_no=0
    c=0
    out_of_keys=0
    for category in os.listdir(directory):
        if(out_of_keys==1):
            break
        path+=category+"/"
        print(category)
        for subcategory in os.listdir(os.path.join(directory,category)):
            
            if(out_of_keys==1):
                break
            currpath=path+subcategory
            
            print(subcategory)
            for keyword in os.listdir(directory+'/'+currpath):
                if(c<startwith):
                    c+=1
                    print(keyword)
                    continue
                # if(stat.GetStatusOfImgData(currpath,keyword)>1000):
                #     continue
                keyword=keyword[:-5] #removing .json
                if(out_of_keys==1):
                    break
                print(c)
                k=stat.Download_KeyWord(currpath,keyword,NUM_PER_KEYWORD,current_key_no)
                c+=1    
                while(k==-1):
                    current_key_no+=1
                    print("Now using api key",current_key_no)
                    if(current_key_no==MAX_API_KEYS):
                        out_of_keys=1
                        break
                    k=stat.Download_KeyWord(currpath,keyword,NUM_PER_KEYWORD,current_key_no)
        path=''

CollectData(KeywordKey_StartIndex)
