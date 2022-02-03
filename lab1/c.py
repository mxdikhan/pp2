def toLowercase(a):
    lower=""
    for i in a:
        if i>="A" and i<="Z":
            lower+=chr(ord(i)+32)
        else:
            lower+=i
    print(lower)
toLowercase(input())