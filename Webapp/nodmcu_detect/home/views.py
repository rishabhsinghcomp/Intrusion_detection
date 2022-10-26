from distutils.command.config import config
from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from pip import main
import pyrebase
from datetime import datetime
from. import firebase_Storage
# pip install pyrebase and pip install urllib3 is required for this setup

# config={
#     "apiKey": "AIzaSyAKRXB4fZREOVDacw9dwehS6PVN4C4dK80",
#     "authDomain": "nodmcuintro.firebaseapp.com",
#     "databaseURL": "https://nodmcuintro-default-rtdb.asia-southeast1.firebasedatabase.app",
#     "projectId": "nodmcuintro",
#     "storageBucket": "nodmcuintro.appspot.com",
#     "messagingSenderId": "278910952430",
#     "appId": "1:278910952430:web:0e6aa04d26d989c6d724ff",
#     "serviceAccount": "serviceAccountCredentials.json"
# }


# firebase=pyrebase.initialize_app(config)
# authe = firebase.auth()
# database=firebase.database()
# storage=firebase.storage()


# def get_intrusion(request):
#     # data=database.child("test").child("int").get().val()
#     # return JsonResponse({"data":data})
#     # only to get date and time
#     ###new method
#     # super_list=[]
#     # data=database.child("test").get()
#     # print(type(data))
#     # print(dict(data))

#     #main_indx=0
#     #print(list(data.val().keys()))
#     # for i in list(data.val().keys()):
#     #     tmp_data=database.child("test").child(i).get()
#     #     super_list.append([i])
#     #     for j in list(tmp_data.val().keys()):
#     #         d = datetime.strptime(j, "%H:%M:%S")
#     #         d = d.strftime("%I:%M:%S %p")
#     #         super_list[main_indx].append(d)
#     #     main_indx+=1


#     ##getting photos only and data
# #     folders=storage.list_files()
# #     blob_obj=[]
# #     super_data=[]
# #     #for collecting requied file name and blobs_objects
# #     for i in folders:
# #         tmp=str(i)[32:]
# #         if(tmp[:4]=="test"):
# #             tmp=tmp[:-1]
# #             blob_obj.append(i)

# #    #creating super_data_set
# #     for i in blob_obj:
# #         tmp=[]
# #         date=str(i)[37:47]
# #         time=str(i)[48:-1]
# #         time = datetime.strptime(time, "%H:%M:%S")
# #         time = time.strftime("%I:%M:%S %p")
# #         i.make_public()
# #         url=i.public_url
# #         tmp=[date,time,url]
# #         super_data.append(tmp)
#     super_data=firebase_Storage.data()

#     return reder({"data":super_data})




def home(request):
    super_data=firebase_Storage.data()
    return render(request,'index.html',{"data":super_data})