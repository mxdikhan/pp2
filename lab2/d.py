n = int(input())
arr = [['.' for i in range(n)] for i in range(n)]

if n % 2 == 0:
    for i in  range(n):
        for j in range(n):
            if i >= j:
                arr[i][j] = '#'
else:
    x = n - 1
    for i in range(n):
        for j in  range(n):
            if j >= x:
                arr[i][j] = "#"
        x = x - 1
            

for i in range(n):
    for j in range(n):
        print(arr[i][j], end = '')
    print()

# 0 0, 0 1, 0, 2 
# 1 0, 1 1, 1, 2
# 2 0, 2 1, 2, 2 
