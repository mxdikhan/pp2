n = int(input())
stud = {}

for i in range(n):
    name, tenge = input().split()
    if name in stud:
        stud[name] = int(stud[name]) + int(tenge)
    else:
        stud[name] = int(tenge)

names2 = sorted(stud.keys())
maxi = max(stud.values())

for x in names2:
    if stud[x] == maxi:
        print(x, " is lucky!")
        #print(f'{x} is lucky!')
    else:
        print(x, " has to receive ", maxi - int(stud[x]), " tenge")
        #print(f'{x} has to receive {maxi - int(stud[x])} tenge')
