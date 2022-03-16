x1, y1 = map(int, input().split())
n = int(input())
ans = []

for i in range(n):
    s = input()
    x2, y2 = s.split()
    d = ((int(x2) - x1) ** 2 + (int(y2) - y1) ** 2) ** 0.5
    ans.append((d, s))

ans.sort()

for x in ans:
    print(x[1])
