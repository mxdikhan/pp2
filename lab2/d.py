n = int(input())
arr = [[0 for i in range(n)] for j in range(n)]
x = n - 1

for i in range(n):
    for j in range(n):
        arr[i][j] = '.'

if n % 2 == 0:
    for i in  range(n):
        for j in range(n):
            if i >= j:
                arr[i][j] = '#'

else:
    for i in range(n):
        for j in  range(n):
            if j >= x:
                arr[i][j] = "#"
        x = x - 1
            

for i in range(n):
    for j in range(n):
        print(arr[i][j], end = '')

    print()