number=int(input())
size=input()
x=0
if size=='k':
    x=int(input())
y= "{:." + str(x) + "f}"
if size=="b":
    number=number*1024
    print(number)
else:
    print(y.format(number/1024))
