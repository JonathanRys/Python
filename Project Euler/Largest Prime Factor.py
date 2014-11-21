def isPrime(number):
    if number % 2 == 0:
        return False
    x = 3
    while x * x <= number:
        if number % x == 0:
            return False
        x += 2
    return True

def factorize(number):
    x = 3
    result = []
    while x * x <= number:
        if number % x == 0:
            result.append(x)
        x += 2
    return result

def largestPrimeFactor(number):
    x = 3
    while x * x <= number:
        if number % x == 0:
            if isPrime(x):
                result = x
        x += 2
    return result

print(largestPrimeFactor(600851475143))
