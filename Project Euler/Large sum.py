def isPrime(number):
    if number % 2 == 0:
        return False
    m = 3
    while m * m <= number:
        if number % m == 0:
            return False
        m += 2
    return True

x = 3
result = 0
while(x < 2000000):
    if isPrime(x):
        result += x
    x += 2

print(result)
