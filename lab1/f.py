amount=int(input())
a=[]
for i in range (amount):
    hour=int(input())
    if hour<=10:
        a.append("Go to work!")
    elif 10<hour<=25:
        a.append("You are weak")
    elif 25<hour<=45:
        a.append("Okay, fine")
    else:
        a.append("Burn! Burn! Burn Young!")
for i in range (amount):
    print(a[i])