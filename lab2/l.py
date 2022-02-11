s = input()
a = []

flag = True
for i in s:
    if i == '{' or i == '[' or i == '(':
        a.append(i)
    elif (len(a) != 0) and (i == '}' or i == ']' or i == ')'):
        if (a[-1] == '{' and i == '}') or (a[-1] == '[' and i == ']') or (a[-1] == '(' and i == ')'):
            a.pop()
        else:
            falg = False
            break

if len(a) != 0:
    flag = False

if flag:
    print("Yes")
else:
    print("No")