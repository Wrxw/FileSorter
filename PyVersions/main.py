import os
import shutil
import time

path = "C:/Users/wikto/Desktop/Sort/"
names = os.listdir(path)
folder_names = ["Images","Text","Apps","Programs"]
Images = 0
Texts = 0
Apps = 0
Programs = 0
for x in range(0,4):
    if not os.path.exists(path+folder_names[x]):
        os.makedirs(path+folder_names[x])
for files in names:
    if ".png" in files and not os.path.exists(path+'Images/'+files):
        shutil.move(path+files, path+'Images/'+files)
        Images = Images+1
    if ".jpg" in files and not os.path.exists(path+'Images/'+files):
        shutil.move(path+files, path+'Images/'+files)
        Images = Images + 1
    if ".jpeg" in files and not os.path.exists(path+'Images/'+files):
        shutil.move(path+files, path+'Images/'+files)
        Images = Images + 1
    if ".gif" in files and not os.path.exists(path+'Images/'+files):
        shutil.move(path+files, path+'Images/'+files)
        Images = Images + 1
    if ".txt" in files and not os.path.exists(path+'Text/'+files):
        shutil.move(path+files, path+'Text/'+files)
        Texts = Texts+1
    if ".pdf" in files and not os.path.exists(path+'Text/'+files):
        shutil.move(path+files, path+'Text/'+files)
        Texts = Texts + 1
    if ".doc" in files and not os.path.exists(path+'Text/'+files):
        shutil.move(path+files, path+'Text/'+files)
        Texts = Texts + 1
    if ".docx" in files and not os.path.exists(path+'Text/'+files):
        shutil.move(path+files, path+'Text/'+files)
        Texts = Texts + 1
    if ".odt" in files and not os.path.exists(path+'Text/'+files):
        shutil.move(path+files, path+'Text/'+files)
        Texts = Texts + 1
    if ".exe" in files and not os.path.exists(path+'Apps/'+files):
        shutil.move(path+files, path+'Apps/'+files)
        Apps = Apps+1
    if ".msi" in files and not os.path.exists(path+'Apps/'+files):
        shutil.move(path+files, path+'Apps/'+files)
        Apps = Apps + 1
    if ".jar" in files and not os.path.exists(path+'Apps/'+files):
        shutil.move(path+files, path+'Apps/'+files)
        Apps = Apps + 1
    if ".ovi" in files and not os.path.exists(path+'Apps/'+files):
        shutil.move(path+files, path+'Apps/'+files)
        Apps = Apps + 1
    if ".py" in files and not os.path.exists(path+'Programs/'+files):
        shutil.move(path+files, path+'Programs/'+files)
        Programs = Programs+1
Sum = Images + Texts + Apps + Programs
print("Found",Images,"Images,",Texts,"Texts,",Apps,"Apps,",Programs,"Programs, totaly sorted files:",Sum)
print("Program will be closed automaticly in 30 secconds ")
time.sleep(30)
print("Godbye")
