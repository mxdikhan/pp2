import os
x=os.access('C:\\Users\\Acer\\OneDrive\\Documents\\pp2', os.F_OK)
if x:
    print('yes')
else:print('no')