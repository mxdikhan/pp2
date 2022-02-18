from cmath import pi
from random import randint
import itertools

def toOunces(grams):
    return grams * 28.3495231

def toCelsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

def solve(heads, legs):
    for rabbits in range(heads):
        if (rabbits * 4 + (heads - rabbits) * 2 == legs):
            return (rabbits, heads - rabbits)
        
def filterPrimes(numbers):
    filteredNumbers = []
    for i in range(len(numbers)):
        isPrime = True
        if (numbers[i] == 1):
            isPrime = False
        for d in range(2, numbers[i]):
            if (numbers[i] % d == 0):
                isPrime = False
        if (isPrime):
            filteredNumbers.append(numbers[i])
    return filteredNumbers

def findAllPermutations(string):
    return list(itertools.permutations(string)) #permutations(list, k) -> if k is not specified, then k == len(list)

def reverse(text):
    words = text.split(' ')
    return list(reversed(words))

def has33(array):
    for i in range(len(array) - 1):
        if (array[i] == 3 and array[i + 1] == 3):
            return True
    return False

def spyGame(array):
    x = False
    y = False
    for i in range(len(array)):
        if (x == False and array[i] == 0):
            x = True
        elif (x == True and y == False and array[i] == 0):
            y = True
        elif (x == True and y == True and array[i] == 7):
            return True
    return False
    
def sphere(radius):
    return 4/3 * pi * radius**3

def uniqueElements(array):
    newArray = []
    for i in range(len(array)):
        if (not array[i] in newArray):
            newArray.append(array[i])
    return newArray

def isPalindrome(word):
    n = len(word)
    for i in range(n):
        if (i > n - i - 1):
            break
        if (word[i] != word[n - i - 1]):
            return False
    return True

def histogram(array):
    for i in range(len(array)):
        print('*' * array[i])
    
def guessTheNumber():
    x = randint(1, 20)
    y = int()
    print('Hello! What is your name?')
    name = input()
    print(f'Well, {name}, I am thinking of a number between 1 and 20')
    print('Take a guess')
    y = int(input())
    t = 1
    while (y != x):
        if (y < x):
            print('Your guess is too low')
            print('Take a guess')
        else:
            print('You guess is too high')
            print('Take a guess')
        y = int(input())
        t = t + 1
    print(f'Good job, {name}! You guessed my number in {t} guesses!')
        

