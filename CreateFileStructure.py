import json
import os
with open("KeywordVisualisation/keyword.json",) as f:
    data=json.load(f)
if not os.path.exists("Data"):
    os.makedirs("Data")
p_folder="Data/"
curr_folder=p_folder
Data=data["children"]
curr_sfolder=""
for category in Data:
    curr_folder=p_folder+category["name"]
    if not os.path.exists(curr_folder):
        os.makedirs(curr_folder)
    for subcategory in category["children"]:
        curr_sfolder=curr_folder+"/"+subcategory["name"]
        if not os.path.exists(curr_sfolder):
            os.makedirs(curr_sfolder)
        for keyword in subcategory["children"]:
            with open(curr_sfolder+"/"+keyword["name"]+".json","w+") as f:
                print(keyword["name"])

if not os.path.exists("ImgData"):
    os.makedirs("ImgData")
p_folder="ImgData/"
curr_folder=p_folder
Data=data["children"]
curr_sfolder=""
for category in Data:
    curr_folder=p_folder+category["name"]
    if not os.path.exists(curr_folder):
        os.makedirs(curr_folder)
    for subcategory in category["children"]:
        curr_sfolder=curr_folder+"/"+subcategory["name"]
        if not os.path.exists(curr_sfolder):
            os.makedirs(curr_sfolder)
        for keyword in subcategory["children"]:
            if not os.path.exists(curr_sfolder+"/"+keyword["name"]):
                os.makedirs(curr_sfolder+"/"+keyword["name"])


if not os.path.exists("ImgRetInd"):
    os.makedirs("ImgRetInd")
p_folder="ImgRetInd/"
curr_folder=p_folder
Data=data["children"]
curr_sfolder=""
for category in Data:
    curr_folder=p_folder+category["name"]
    if not os.path.exists(curr_folder):
        os.makedirs(curr_folder)
    for subcategory in category["children"]:
        curr_sfolder=curr_folder+"/"+subcategory["name"]
        if not os.path.exists(curr_sfolder):
            os.makedirs(curr_sfolder)
        for keyword in subcategory["children"]:
            with open(curr_sfolder+"/"+keyword["name"]+".txt","w+") as f:
                f.write("1")
