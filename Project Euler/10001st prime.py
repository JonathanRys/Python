def isPrime(number):
    i = 3
    if number % 2 == 0: return False
    while i * i <= number:
        if number % i == 0: return False
        i += 2
    return True
        
def getNthPrime(stopNum):
    index = 1
    n = 1
    while index < stopNum:
        n += 2
        if isPrime(n):
            index += 1
    return n

print(getNthPrime(10001))

