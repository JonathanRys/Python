import time

def factorize(number):
    x = 1
    result = []
    while x * x <= number:
        if number % x == 0:
            result.append(x)
            if x * x != number:
                result.append(int(number / x))
        x += 1
    return result

def getTriFactor(numFactors):
    index = 1
    triangle = 0
    while True:
        triangle += index
        factors = factorize(triangle)
        if len(factors) > numFactors:
            return triangle
        index += 1

startTime = time.time()
print(getTriFactor(500), "\nTime elapsed:", time.time() - startTime)

#>>>
#76576500 
#Time elapsed: 35.952468156814575
#>>>
