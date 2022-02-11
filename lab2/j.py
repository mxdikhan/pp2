n = int(input())
strong = []

def ans(s):
    num = False
    up = False
    low = False
    for i in s:
        if i >= '0' and i <= '9':
            num = True
        if i >= 'A' and i <= 'Z':
            up = True
        if i >= 'a' and i <= 'z':
            low = True
    if num and up and low:
        return True
    else: 
        return False

for i in range(n):
    pas = input()
    if ans(pas) and pas not in strong:
        strong.append(pas)

strong.sort()

print(len(strong))
for x in strong:
    print(x)