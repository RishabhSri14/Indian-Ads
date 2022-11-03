from googleapiclient.discovery import build
import json
import gspread
import json
import os
import time
from GetData import ExtractData
from GoogleSpreadsheet import utilities as gs

def GetNumberOfImages(cat,subcat,k):
    with open('./../data/{}/{}/{}'.format(cat,subcat,k+' Indian Ads.json'), 'r') as f:
            data = json.load(f)
    c=0
    for dat in data:
        c+=1
    print (c)
    return c

spread =gs("Visual Metaphors KeyWords","Indian Ads KeyWords")
dict ={}
# dict['name']="Keywords"
# dict['children']=[]
with open('./../KeywordVisualisation/data.json','r') as f:
    dict=json.load(f)
current_cat=7
i=3868
# current_cat=-1
current_cat_name=None
current_subcat_name=None
current_subcat=-1
# i=3
while(i<=4057):
    time.sleep(2)
    cat=spread.w.cell(i,1).value
    subcat=spread.w.cell(i,2).value
    k=spread.w.cell(i,3).value
    if(cat!=None):
        dict['children'].append({'name':cat, 'children':[]})
        current_cat+=1
        current_cat_name=cat
        current_subcat=-1
    if(subcat!=None):
        (dict['children'])[current_cat]['children'].append({'name':subcat, 'children':[]})
        current_subcat_name=subcat
        current_subcat+=1
    if(k!=None):
        dict['children'][current_cat]['children'][current_subcat]['children'].append({'name':k,'size':GetNumberOfImages(current_cat_name,current_subcat_name,k)})
    with open('./../KeywordVisualisation/keyword.json', 'w') as f:
        json.dump(dict,f)
    print(i, cat," ", subcat," ", k)
    i+=1





    

    
    