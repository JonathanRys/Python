#!/usr/bin/python

from time import time, ctime
from datetime import timedelta
from gmpy2 import is_prime, next_prime

def Store(data):
    with open("PrimeMersenneNumbers.txt", "a") as primes:
        primes.write(str(data)+"\n\n")

def ConfirmPrimality(data):
    for primes in primeNumbers:
        if primes^2>data: return True
        if data%primes==0: return False
    return True

def SetFileInfo();
    with open("PrimeMersenneNumbers.txt", "a") as primes:
        primes.write(ctime()+"\n")
        primes.write("The following numbers from 2^"+str(startNum)+" to 2^"+str(endNum)+" are prime:\n")
    print(".", end="")

def LoadValues(fileName);
    with open(fileName, "r") as primes:
        for i in primes:
            num.append(i)
    print(".", end="")
    num.pop(0)
    num=[int(i) for i in num]
    return num

#Program starts here ###
print("This program calculates Mersenne primes (2^n -1).")
while True:
    try:
        startNum=int(input("Please enter a number (2^no.) to begin testing at: "))
        endNum=int(input("Please enter a number (2^no.) to end testing at: "))
        break
    except ValueError:
        print("Illegal value entered.")
print("Loading.", end="")
SetFileInfo()
primeNumbers=LoadValues()
print("done.\n")

startTime=time()
while startNum<=endNum:
    testNum=(2**startNum) - 1
    if is_prime(testNum):
        print("Candidate found: 2^", startNum)
        #if ConfirmPrimality(testNum):
        Store(testNum)
    #startNum+=2 #test every number
    startNum=next_prime(startNum) #only test with prime exponents
print("Time Elapsed:", timedelta(seconds=time()-startTime))
Store("Time Elapsed:"+ str(timedelta(seconds=time()-startTime)))
