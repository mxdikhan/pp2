import os
path='C\\Users\\Acer\\OneDrive\\Documents\\pp2'
if os.path.exists(path):
    print(os.path.basename(path))
    print( os.listdir(path))
else: print("NO")
