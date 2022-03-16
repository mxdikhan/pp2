s = input()
a = []

flag = True
for i in s:
    if i == '{' or i == '[' or i == '(':
        a.append(i)
    elif (len(a) != 0):
        if (a[len(a) - 1] == '{' and i == '}') or (a[len(a) - 1] == '[' and i == ']') or (a[len(a) - 1] == '(' and i == ')'):
            a.pop()
        else:
            flag = False
            break

if len(a) != 0:
    flag = False

if flag:
    print("Yes")
else:
    print("No")