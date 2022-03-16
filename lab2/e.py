s = input().split()
if len(s) == 1: s.append(input())
n, x, k = int(s[0]), int(s[1]), 0
arr = []
for i in range(n):
    arr.append(x + 2*i)
    k = k ^ arr[i]
print(k)


