dish=input()
length=len(dish)
tastyness=0
for i in range (length):
    tastyness+=ord(dish[i])
if tastyness<300:
    print("Oh, no!")
else: 
    print("It is tasty!")