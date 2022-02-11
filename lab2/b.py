a = int(input())
b = []
for i in input().split():
    b.append(int(i))

for i in range(len(b)):
    b.sort()
    b.reverse()
    v = b[0] * b[1]

print(v)

