import gspread
import json
import time
import os
class utilities:
    def __init__(self,FileName,WorksheetName):
        key1='../ServiceAccounts_Keys/visual-metaphors1.json'
        key2='../ServiceAccounts_Keys/visual-metaphors2.json'
        key3='../ServiceAccounts_Keys/visual-metaphors3.json'
        key4='../ServiceAccounts_Keys/visual-metaphors4.json'
        key5='../ServiceAccounts_Keys/visual-metaphors5.json'
        sa=gspread.service_account(key1)
        self.f= sa.open(FileName)
        self.w=self.f.worksheet(WorksheetName)

    def Check_FileStructure(self, path):
        if not os.path.exists("../data/"+path):
            os.makedirs("../data/"+path)
    
    def AddExample(self, path, keyword):
        firstWord=keyword.find(" ")
        lastWord=keyword.rfind(" ")
        k=keyword.find("Indian Ads")
        key=""
        if(keyword!="Indian Coffee House Indian Ads"and keyword!="Indian Bean Indian Ads" and keyword[0:firstWord] =="Indian" and keyword[lastWord+1:] =="Ads"):
            key=keyword[firstWord+1:lastWord]
        else:
            key=keyword[0:k-1]

        print("Updating Spreadsheet with some examples of "+key)
        row_no=self.w.find(key).row
        self.Check_FileStructure(path)
        with open('./../data/{}/'.format(path)+keyword+'.json', 'r') as f:
            data = json.load(f)
        sno=row_no
        for dat in data:
            time.sleep(3)
            self.w.update_cell(sno,4,dat['title'])
            self.w.update('E{}'.format(sno),'=IMAGE("{}",2)'.format(dat['Image']),raw=False)
            self.w.update_cell(sno,6,dat['Taken From'])
            sno+=1
            if(sno!=row_no+10):
                self.w.insert_row(["" for cell in range(self.w.col_count)],sno)
            if(sno>=row_no+10):
                break
        print("Spreadsheet Updated")
    

    def GetListOfKeywords(self,path):
        list_of_keywords=[]
        c=0
        ind= path.find("/")
        subcat=path[ind+1:]
        cell=self.w.find(subcat)
        i= cell.row
        while(1):
            # time.sleep(3)
            k=self.w.cell(i,3).value
            print(k)
            if((k=="" or k==None) and c==1):
                break
            elif((k=="" or k==None) and c==0):
                c+=1
                list_of_keywords.append("Indian "+subcat+" Ads")
            else:
                list_of_keywords.append(self.w.cell(i,3).value +" Indian Ads")
            i+=1
        return list_of_keywords


            

