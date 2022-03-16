s=str(input())
q=input()
x=s.find(q)
y=s.rfind(q)
if(x==y):
    print(x)
else:print(x, y)


