x1, y1 = map(int, input().split())
n = int(input())
ans = []

def srt(f):
    return f[1]

for i in range(n):
    s = input()
    x2, y2 = s.split()
    d = ((int(x2) - x1) ** 2 + (int(y2) - y1) ** 2) ** 0.5
    ans.append((s, d))

ans.sort(key = srt)

for x in ans:
    print(x[0])