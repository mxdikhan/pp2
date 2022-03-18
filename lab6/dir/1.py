import os
path='C:\\Users\\Acer\\OneDrive\\Documents\\pp2'
list=os.listdir(path)
dirlist=[]
filelist=[]

for name in list:
    if os.path.isdir(os.path.join(path,name)):
        dir.append(name)
    elif os.path.isfile(os.path.join(path,name)) :
        filelist.append(name)

print("Directories",dirlist,"\n""Files",filelist, "\n""All", list)
