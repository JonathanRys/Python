#!/usr/bin/python

from time import time
import gmpy2
from math import sqrt
def isqrt(n):
    x = n
    y = (x + n // x) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def Read(data):
    fileName="PrimeNumbers.txt"
    file=open(fileName,"r") 
    x=file.read(data)
    file.close
    return x

def Store(data):
    fileName="PrimeNumbers.txt"
    file=open(fileName,"w") 
    file.write(data)
    file.close
    print("File: "+fileName+" saved successfully.")

def ConfirmPrimality(data):
    #read from file of generated primes first
    #and only test for divisibility by primes
    j=2
    if data%2==0: return False
    j=3
    maxVal=isqrt(data)+1
    while j <= maxVal:
        if data%j==0:
            print(str(data)+" is not Prime")
            return False
        j+=2
    return True

while True:
    try:
        startNum=int(input("Please enter a power (2^x) to begin testing at: "))
        endNum=int(input("Please enter a power (2^x) to end testing at: "))
        break
    except ValueError:
        print("Illegal value entered.")

primes=[]
i=0
startTime=time()
while startNum<=endNum:
    testNum=(2**startNum) - 1
    print(startNum, testNum)
    if gmpy2.is_prime(testNum):
        print("is probably prime")
        if ConfirmPrimality(testNum):
            print("is prime")
            primes.append(testNum)
            i+=1
    startNum+=1 #test every number
    #startNum=gmpy2.next_prime(startNum) #only test with prime exponents
print("Time Elapsed: "+str(time() - startTime))
number=""
output=""
for number in primes:
    output=output+str(number)+", "
Store(output[:-2])
