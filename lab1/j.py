s=input().split()
a=[]
for i in s:
    if len(i)>=3:
        a.append(i)
        
x=" ".join(a)
print(x)