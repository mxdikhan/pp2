from math import sqrt

class MyStrings:
    def getString(self):
        self.string = input()
    def printString(self):
        print(self.string)

frt = MyStrings()
frt.getString()
frt.printString()

class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
        super().__init__()
    
    def area(self):
        return self.length * self.length

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        super().__init__()

    def area(self):
        return self.length * self.width

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(self.x, self.y)

    def move(self, newX, newY):
        self.x = newX
        self.Y = newY

    def dist(self, x, y):
        print(sqrt((self.x - x)**2 + (self.y - y)**2))

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, sum):
        self.balance = self.balance + sum
    
    def withdraw(self, sum):
        if (self.balance >= sum):
            self.balance = self.balance - sum




def isPrime(x):
    if (x == 1):
        return False
    for i in range(2, x):
        if (x % i == 0):
            return False
    return True

#array = list(map(int(), input().split()))
#array = list(filter(lambda x: isPrime(x), array))
#print(array)
