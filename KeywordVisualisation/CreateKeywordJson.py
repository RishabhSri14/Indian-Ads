import json
import os

directory = "../Data/"
path=''
c=0
dic={"name":"Keyword","children":[]}


for category in os.listdir(directory):
    a={"name":category,"children":[]}
    path=directory+category+"/"
    print()
    print(category)
    print()
    
    for subcategory in os.listdir(os.path.join(directory,category)):
        print()
        print(subcategory)
        print()
        b={"name":subcategory,"children":[]}
        k=0
        currpath=path+subcategory
        for keyword in os.listdir(directory+'/'+currpath):
            b["children"].append({"name":keyword[:-5],"size":10})
        a["children"].append(b)
    dic["children"].append(a)

with open("keyword.json","w+") as f:
    json.dump(dic,f)


                        
