def collatzChain(number):
    chain = [number]
    while number > 1:
        if number % 2 == 0:
            number /= 2
        else:
            number = ((3 * number) + 1)
        chain.append(number)
    return chain

longest = 0
for x in range(1000000):
    if len(collatzChain(x)) > longest:
        longest = len(collatzChain(x))
        start = x
print(start, longest, collatzChain(start))
