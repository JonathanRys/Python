n = 3
result = 0
while n * n <= 600851475143:
    if 600851475143 % n == 0:
        print(n)
        m = 3
        fail = False
        while m * m <= n:
            if n % m == 0:
                print("failing ", n, m)
                fail = True
                break
            m += 2
        if fail == False:
            result = n
    n += 2

print(result)
