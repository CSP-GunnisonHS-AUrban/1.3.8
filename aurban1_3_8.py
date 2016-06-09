'''
Programmer: Alex Urban
06.08.2016
Compiler: Canopy 1.7.2
aurban1_3_8
'''

from __future__ import print_function
import random

def days():
    ''' This will give me the day of the week!'''
    for day in 'MTWRFSS':
        print(day + 'day')
    for day in range(5,8):
        print('It is the ' + str(day) + 'th of September')
        
        
import matplotlib.pyplot as plt
plt.ion()

def picks():
    a = [] #empty list
    
    a += [random.choice([1,3,10])]
    
    for choices in range(5):
        a += [random.choice([1,3,10])]
        
    plt.hist(a)
    plt.show()
    
def rollHundredPair():
    
    rollList = []
    
    for rolls in range(99):
        rollList += [random.choice([1,2,3,4,5,6])]
        #print(rollList)
        
    plt.hist(rollList)
    plt.show
    
def dice(n):
    
    sumList = []
    diceSum = 0
    for items in range(n):
        sumList += [random.choice([1,2,3,4,5,6])]
        print(sumList)
    diceSum = sum(sumList)
    print(diceSum)
    
def hangmanDisplay(guessed, secret):
    secretHang = ''
    for char in secret:
        if char in guessed:
            secretHang = secretHang + char
        else:
            secretHang = secretHang + '_'
    print(secretHang)


def matches(ticket, winners):
    count = 0
    for number in winners:
        if number in ticket:
            count += 1
    print(count)
    
    
def report(guess, secret):
    rightColor = 0
    wrongPlace = 0
    for color in secret:
        if color in guess:
            rightColor += 1
    for place in secret:
        if guess[place] not in secret[place]:
            wrongPlace += 1
    print(rightColor)
    print(wrongPlace)
            