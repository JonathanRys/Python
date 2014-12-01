def factorial(num):
    retVal = 1
    for x in range(num):
        retVal *= (x + 1)
    return retVal

stringNum = str(factorial(100))
counter = 0
for x in stringNum:
    counter += int(x)
print(counter)
