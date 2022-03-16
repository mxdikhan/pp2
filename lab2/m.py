a = []

def srt(f):
    return f[2], f[1], f[0]

while True:
    date = input().split()
    if date[0] == '0':
        break
    a.append((date[0], date[1], date[2]))

a.sort(key = srt)
for i in a:
    print(i[0], i[1], i[2])