n = int(input())
discs = []
res = []

for i in range(n):
    x = input().split()
    if int(x[0]) == 1:
        discs.append(x[1])
    elif int(x[0]) == 2:
        res.append(discs[0])
        discs.pop(0)

for i in res:
    print(i, end = ' ')