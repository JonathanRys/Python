def sumOfSquares(number):
    retVal = 0
    for i in range(1, number + 1):
        retVal += i * i
    return retVal

def squareOfSums(number):
    retVal = 0
    for i in range(1, number + 1):
        retVal += i
    return retVal * retVal

value = 100
print(abs(squareOfSums(value) - sumOfSquares(value)))
