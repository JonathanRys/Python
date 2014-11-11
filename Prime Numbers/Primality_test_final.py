#!/usr/bin/python

from datetime import datetime
from gmpy2 import next_prime

def Store(data):
    fileName="PrimeNumbers.txt"
    file=open(fileName,"w") 
    file.write(data)
    file.close
    print("File: "+fileName+" saved successfully.")
    return True

#Ask for start and end numbers
while True:
    try:
        startNum=int(input("Please enter a number to begin testing at: "))
        break
    except ValueError:
        print("Illegal value entered.")
while True:
    try:
        endNum=int(input("Please enter a number to end testing at: "))
        break
    except ValueError:
        print("Illegal value entered.")
#Set variables
result="The following numbers between "+str(startNum)+" and "
primes=[]
flgPrime=True
primeList=""
#Start Timer
startTime=datetime.now()
#If the starting number is less than 2, then add "2" to the list of primes.
if startNum<4:
    primeList="2\n"
    if endNum>2:
        primeList+="3\n"
        startNum=5
#If startNum is even add 1
elif startNum%2 in [0]:
    startNum+=1
#Cycle through odd numbers in the given range
for i in range(startNum, endNum+1,2):
    flgPrime=True
    #We know that the number isn't divisible by 2 (^Ibed),
      #so only test with odd numbers up to j squared.
    j=3
    while i>=j*j:
        #if i is divisible by j then stop testing the current value.
        if i%j in [0]:
            flgPrime=False
            break
        #Otherwise, increment j by 2.
        j=next_prime(j)
    #If the number is prime, add it to the list.
    if flgPrime:
        primes.append(i)
#Output results:
print("Time Elapsed:", datetime.now() - startTime, end="")
print(" - converting",len(primes),"strings.")
#Convert numbers to strings
for num in primes:
    primeList+=str(num)+"\n"
#Report progress
result+=str(endNum)+" are prime:\n"+primeList
print("Strings converted:", datetime.now() - startTime)

#Write to file
Store(result[:-1])
print("Total Time Elapsed:", datetime.now() - startTime)
