jump=input().split()
list=[]
for i in range (len(jump)):
    list.append(int(jump[i]))
max_jump=0
for i in range (len(jump)):
    if max_jump>=i:
        if list[i]+i>=len(jump)-1:
            print(1)
            exit()
        elif list[i]+i>max_jump:
            max_jump=list[i]+i
    else:
        break
if max_jump<len(jump)-1:
    print(0)