n = int(input())
arr = [[0 for i in range(n)] for i in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            arr[i][j] = i ** 2
        elif i == 0 and j != 0:
            arr[i][j] = j
        elif i != 0 and j == 0:
            arr[i][j] = i

for i in range(n):
    for j in range(n):
        print(arr[i][j], end = ' ')
    print()

# pow(x, y) ~ x**y