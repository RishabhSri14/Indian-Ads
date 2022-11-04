import pandas as pd
import os
df= pd.read_csv("Add.csv")
if not os.path.exists("Data"):
    os.makedirs("Data")
p_folder="Data/"
curr_folder=p_folder
for index, x in df.iterrows():
    if(x['Type']=='HEAD'):
        curr_pfolder=p_folder+x["O_name"]+"/"
        if not os.path.exists(curr_pfolder):
            os.makedirs(curr_pfolder)
        print(curr_pfolder)
    elif(x['Type']== 'SUBHEAD'):
        curr_sfolder=curr_pfolder+x['O_name']+"/"
        if not os.path.exists(curr_sfolder):
            os.makedirs(curr_sfolder)
        print(curr_sfolder)
    elif(x['Type']=='KEYWORD'):

        print(x['N_name'])
        if(x['N_name']!=float("NaN") and str(x['N_name'])!="" ):
            try:
                with open(curr_sfolder+x['N_name']+".json",'w+') as f:
                    print(curr_sfolder+x['N_name']+".json")
            except Exception as e:
                print(e)
    
if not os.path.exists("ImgData"):
    os.makedirs("ImgData")
p_folder="ImgData/"
curr_folder=p_folder
for index, x in df.iterrows():
    if(x['Type']=='HEAD'):
        curr_pfolder=p_folder+x["O_name"]+"/"
        if not os.path.exists(curr_pfolder):
            os.makedirs(curr_pfolder)
        print(curr_pfolder)
    elif(x['Type']== 'SUBHEAD'):
        curr_sfolder=curr_pfolder+x['O_name']+"/"
        if not os.path.exists(curr_sfolder):
            os.makedirs(curr_sfolder)
        print(curr_sfolder)
    elif(x['Type']=='KEYWORD'):

        print(x['N_name'])
        if(x['N_name']!=float("NaN") and str(x['N_name'])!="" ):
            try:
                os.mkdir(curr_sfolder+x['N_name'])
            except Exception as e:
                print(e)

if not os.path.exists("ImgRetInd"):
    os.makedirs("ImgRetInd")
p_folder="ImgRetInd/"
curr_folder=p_folder
for index, x in df.iterrows():
    if(x['Type']=='HEAD'):
        curr_pfolder=p_folder+x["O_name"]+"/"
        if not os.path.exists(curr_pfolder):
            os.makedirs(curr_pfolder)
        print(curr_pfolder)
    elif(x['Type']== 'SUBHEAD'):
        curr_sfolder=curr_pfolder+x['O_name']+"/"
        if not os.path.exists(curr_sfolder):
            os.makedirs(curr_sfolder)
        print(curr_sfolder)
    elif(x['Type']=='KEYWORD'):

        print(x['N_name'])
        if(x['N_name']!=float("NaN") and str(x['N_name'])!="" ):
            try:
                with open(curr_sfolder+x['N_name']+".txt",'w+') as f:
                    f.write("1")
                    print(curr_sfolder+x['N_name']+".txt")
            except Exception as e:
                print(e)

