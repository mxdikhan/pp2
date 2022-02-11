s = input()
s = s.replace('?', ' ').replace(',', ' ').replace('!', ' ').split()

res = []

for i in s:
    if i not in res:
        res.append(i)

res.sort()

print(len(res))
for x in res:
    print(x)