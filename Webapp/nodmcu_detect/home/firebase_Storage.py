
from cgi import print_form
from time import process_time_ns, time
import pyrebase
from datetime import datetime


config={
    "apiKey": "AIzaSyAKRXB4fZREOVDacw9dwehS6PVN4C4dK80",
    "authDomain": "nodmcuintro.firebaseapp.com",
    "databaseURL": "https://nodmcuintro-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "nodmcuintro",
    "storageBucket": "nodmcuintro.appspot.com",
    "messagingSenderId": "278910952430",
    "appId": "1:278910952430:web:0e6aa04d26d989c6d724ff",
    "serviceAccount": "/home/rishabh/Desktop/Arduino/NodMcuTesting/WEBAPP/TESTING/serviceAccountCredentials.json"
}


def data():
    firebase=pyrebase.initialize_app(config)
    authe = firebase.auth()
    database=firebase.database()


    storage=firebase.storage()
    folders=storage.list_files()


    blob_obj=[]

    #for collecting requied file name and blobs_objects
    for i in folders:
        tmp=str(i)[32:]
        if(tmp[:4]=="test"):
            tmp=tmp[:-1]
            blob_obj.append(i)


    super_data=[]
    for i in blob_obj:
        tmp=[]
        date=str(i)[37:47]
        time=str(i)[48:-1]
        time = datetime.strptime(time, "%H:%M:%S")
        time = time.strftime("%I:%M:%S %p")
        i.make_public()
        url=i.public_url
        tmp=[date,time,url]
        super_data.append(tmp)


    print(super_data)
    return super_data



    # for i in  blob_obj:
    #     i.make_public()
    #     print(i.public_url)




