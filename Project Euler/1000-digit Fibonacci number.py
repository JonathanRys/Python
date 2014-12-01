from math import sqrt
phi = (1 + sqrt(5))/2

def nthFib(n):
    return int((phi**n - (-phi**-n))//sqrt(5))

counter = 4
oldFib = 2
fib = 3
while True:
    newFib = fib + oldFib
    oldFib = fib
    fib = newFib
    counter += 1
    if len(str(fib)) >= 1000:
        print(counter, ':', fib)
        break
