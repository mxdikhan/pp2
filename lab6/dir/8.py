import os
path='C:\\Users\\Acer\\OneDrive\\Documents\\pp2\\lab6\\test\\for_del.txt'
if os.access(path, os.F_OK):
    os.remove('for_del.txt')
    print('File deleted')
else:
    print('File do not exist')