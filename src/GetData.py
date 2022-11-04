from ast import keyword
import imghdr
from shutil import copyfileobj
from googleapiclient.discovery import build
import json
import time
import requests
import os
from PIL import Image
import status 
import shutil
ImgPerPage=10
class ExtractData:
    def __init__(self,list_of_words,Num):
        self.KeyWords=list_of_words
        self.N=Num
    
    #Get a list of images from google search
    def get_images(self,key_word,i, SearchStartIndex):
        api_key=[]
        api_key.append("AIzaSyCvp5ragLW63x74JfLf3qzi0lHxAoGPME8")#0
        api_key.append("AIzaSyAwkXXxzvoIk3kKxgT_Co8DWavuHmHRmzQ")#1
        api_key.append("AIzaSyBC4IVl4_r1WSwZann3gmth2EX-FXzrg08")#2
        api_key.append("AIzaSyAjAgjWCPkbJsSvXAtINb8JzsmGGVZI1T4")#3
        api_key.append("AIzaSyC1jT5KY7FrRyniIbEv4IFH-kkmWvCoZTs")#4
        api_key.append("AIzaSyCpcrHtpCmS6536AGjpfiOF8IPx7vrthQM")#5
        api_key.append("AIzaSyBke3C_lCzrSjahyw3GJFGHpadiBXuE1oI")#6
        api_key.append("AIzaSyBZQTA_dpZaa_cVWJEOXdUnNwCNh1Xv8jQ")#7
        api_key.append("AIzaSyC5fKitDgVNCai9Qsg4f7yVc33RnDaHKWs")#8
        api_key.append("AIzaSyCiHxLmLpMOZ4Hm60kQqy9P77nAqG82CUw")#9
        api_key.append("AIzaSyC_Ce56Dfc6iEmhWnwftWciD7VQTUH_O7E")#10
        api_key.append("AIzaSyBKEnSq4z5BfW4nuniLQ1vDozIpTtgCx4o")#11
        api_key.append("AIzaSyADzO5FUGqPQ6v4-XYMxvKTZW8cCvg_VGg")#12
        api_key.append("AIzaSyCch-uJDWBRQ_sLwk4MfkM2p3wF7VxlL90")#13
        api_key.append("AIzaSyAqyiZBsn8fAcASh275w8k5jmCy-y6yELw")#14
        api_key.append("AIzaSyDKNd-f57IgT1WG0ohtB2wPEHe-VoYWTD8")#15
        api_key.append("AIzaSyAg0xg5O9n3osHXZQOHKtNisLagCFiNvlc")#16
        api_key.append("AIzaSyDsUJcyGdBajEiHqzyNaENpm0BbcisstO8")#17
        api_key.append("AIzaSyDMOdu7WMtYmnbQm08178NkyLPobDuPg0M")#18
        api_key.append("AIzaSyDAU9YuIGweBODzfHlBNQLPZijgdyBOcmc")#19
        api_key.append("AIzaSyDlgIC5lmuPLgtY3LifNNtMAiHhpnVC2zc")#20
        api_key.append("AIzaSyDQoiRjE9TmMUYeFMLsf_5sB1jbELxXVec")#21
        api_key.append("AIzaSyDmW5uFMEC5AIYebhoTy6AipboOvFtMsr8")#22
        api_key.append("AIzaSyDpI_aXYQIkFMhS0R3yYsTsDiWF3dNnsN4")#23
        api_key.append("AIzaSyAlRwCTO9y2r18VFKYtsEPnDNewRkfNIfY")#24
        api_key.append("AIzaSyCUY2U8DnMoXJDLvhHT3xdA_M4uE5tXMqE")#25
        api_key.append("AIzaSyBYXbLcQpaMGWdK6TcFfeqnVH8i9TKeDbE")#26
        api_key.append("AIzaSyAb5YY1d4fwOcD0EjmzsUVBfPM1t-E4Yec")#27
        api_key.append("AIzaSyDFxQWJcGmbLoyKsDo8KG6Qrfc7RqpPIBE")#28
        api_key.append("AIzaSyAfFHasjqrzJevooWm617wR6QNhP0djV1I")#29
        api_key.append("AIzaSyA3OIR4ajnutAOlHHcTtVN4KCPIPTsqV9Y")#30
        api_key.append("AIzaSyCI12Jt4YWWZBhAi-czxUITzKZBJDJbYW4")#31
        api_key.append("AIzaSyDUNYgcXIepGmz88Z69I9acd1mCJLumZCA")#32
        api_key.append("AIzaSyA_ovw4L1NfKwEvvoUthhgDYJRn3Do_UbM")#33
        api_key.append("AIzaSyDKGa4bd7SQbAzL_qOh_l9QmkI7BPwHZCM")#34
        api_key.append("AIzaSyAQurKy-QWd5rT9XDXMNuItAoBsCCpF-gU")#35
        api_key.append("AIzaSyB6DjfJyS8VLHnfwEHO91It0FOmNu7VeWc")#36
        api_key.append("AIzaSyBwxEZF6yzpstLn5mSMPTN6rMqsi1KchLA")#37
        api_key.append("AIzaSyBw12OpYE_qu4Zxz_Ixx-gBS1jNVcHKR4A")#38
        api_key.append("AIzaSyCFkgM1VnVuVJUEgiJNKPE7M33Dnr_4lTU")#39
        api_key.append("AIzaSyBDZN_LcIrvwzC_5GWrxCfIJeTIveNpRHE")#40
        api_key.append("AIzaSyCMM6aU7eH5eIv7ps_TzzlRPUKF0sc-Z4A")#41
        api_key.append("AIzaSyASyz9xmTMdPkVxM973i8yf7Lc-YsXl2rc")#42
        api_key.append("AIzaSyAVRqhV8zmqI6XAEWtehI_mnihZO4INgFk")#43
        api_key.append("AIzaSyCbYlIqngnZcuV_oR5_WLrEWafsyShqpQM")#44
        api_key.append("AIzaSyA4_GckyeUsVwia61IWncApH7TB6G97R7k")#45
        api_key.append("AIzaSyCE6nSLbErp5JtqMf0jeT14emmZEDDJaFk")#46
        api_key.append("AIzaSyBjWS3n2JcbLBXg5j-HSQ_dBzzLNxgZXgM")#47
        c_x='c0a4e8306fc3d4afe'
        resource = build("customsearch", 'v1', developerKey=api_key[i]).cse()
        images = []
        for i in range(int(SearchStartIndex),int(SearchStartIndex)+ self.N, ImgPerPage):
            try:
                result = resource.list(q=key_word, cx=c_x, searchType='image', start=i).execute()
            except Exception as e:
                print(e)
                return -1
            images += result['items']
        return images

    def download_image(self,path,i):
        if not os.path.exists("../Data/"+path):
            os.makedirs("../Data/"+path)
        for ind in range(len(self.KeyWords)):
            num=0
            with open("../ImgRetInd/"+path+"/"+self.KeyWords[ind]+".txt",'r') as f:
                num=int(f.read())

            images=self.get_images(self.KeyWords[ind],i,num)
            
            if(images==-1):
                return -1
            else:
                with open("../ImgRetInd/"+path+"/"+self.KeyWords[ind]+".txt",'w+') as f:
                    f.write(str(self.N+num))
            req_dat=[]
            c=num
            for item in images:
                req_dat.append({"Sno":c, "title":item['title'], "Image":item['link'], "Taken From":item['image']['contextLink']})
                c+=1
            
            # Writing Json data of images in Data
            data=[]
            with open('../Data/{}/{}.json'.format(path,self.KeyWords[ind]), ) as fp:
                if(os.stat('../Data/{}/{}.json'.format(path,self.KeyWords[ind])).st_size != 0):
                    data=json.load(fp)
                    data.extend(req_dat)
                else:
                    data=req_dat
            with open('../Data/{}/{}.json'.format(path,self.KeyWords[ind]),'w' ) as fp:
                json.dump(data,fp)

            # Downloading the images in Dat_img
            for item in req_dat:
                try:
                    res=requests.get(item['Image'],stream=True)
                    if(res.status_code==200):
                        print("Downloading img" + str(item['Sno']) +"...")
                        Images_filename="../images/"+self.KeyWords[ind]+"_"+str(item['Sno']) +".jpg"
                        with open(Images_filename,"wb") as f:
                            copyfileobj(res.raw,f)
                        te=imghdr.what(Images_filename)
                        if(imghdr.what(Images_filename)!=None):
                            Dat_filename="../ImgData/"+path+"/"+self.KeyWords[ind]+"/"+self.KeyWords[ind]+"_"+str(item['Sno'])+"."+te
                            shutil.copyfile(Images_filename,Dat_filename)
                            # with open(Dat_filename,"wb") as f:
                            #     copyfileobj(res.raw,f)
                            if(te=="webp"):
                                im=Image.open(Dat_filename).convert("RGB")
                                im.save("../ImgData/"+path+"/"+self.KeyWords[ind]+"/"+self.KeyWords[ind]+"_"+str(item['Sno'])+".jpg","jpeg")
                                os.remove("../ImgData/"+path+"/"+self.KeyWords[ind]+"/"+self.KeyWords[ind]+"_"+str(item['Sno'])+"."+te)
                        # os.rename("../Dat_img/"+self.KeyWords[ind]+"/"+self.KeyWords[ind]+"_"+str(item['Sno']) +".jpg",Dat_filename)
                        print(f'Downloaded... ')

                except Exception as e:
                    print("Oh no",e)


            
            