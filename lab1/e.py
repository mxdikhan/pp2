def dis(n):
     for i in range(2, int(n/2)+1):
        if n%i==0:
          return False
     return True 
s= input().split()   
d= int(s[0])
c= int(s[1])
if (d < 500 and dis(d) == True and c % 2==0):
     print("Good job!")
else: print("Try next time!")