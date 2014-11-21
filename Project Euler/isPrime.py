def isPrime(number):
    if number % 2 == 0:
        return False
    m = 3
    while m * m <= number:
        if number % m == 0:
            return False
        m += 2
    return True
