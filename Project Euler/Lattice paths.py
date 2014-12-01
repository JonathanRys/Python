def factorial(num):
    retVal = 1
    for x in range(num):
        retVal *= (x + 1)
    return retVal

def latticePaths(number):
    return int((factorial(2 * number))/(factorial(number) * factorial(number)))

print(latticePaths(20))
