from random import randrange


def squares():
    i : int = 1
    while i**2 < 2000:
        print(i**2)
        i+=1
        
def factorial():
    inp = int(input("Enter integer: "))
    i = 1
    total = 1
    while i <= inp:
        total = total * i
        i += 1
    print(total)
    
def investment():
    initial = int(input("Initial investment: "))
    target = int(input("Target Value: "))
    rate = int(input("Interest Rate: "))
    current = initial
    i = 0
    while current < target:
        current = current + (current * (rate / 100))
        print(current)
        i += 1
    print(i)    
    
def intGuess():
    max = randrange(75,100)
    min = randrange(1, 25)
    guessNo = 0
    guesscap = 3
    while guessNo < guesscap:
        guess = int(input("Enter a number: "))
        if guess > min and guess < max:
            print("Correct")
            break
        else:
            print("Nope")
            guessNo += 1
            None
        
def countVowels():
    word = str(input("Enter a word: "))
    vowls = ("a","e","i","o","u")
    count = 0
    for letter in word:
        if letter in vowls:
            count += 1
    print(count)
    







