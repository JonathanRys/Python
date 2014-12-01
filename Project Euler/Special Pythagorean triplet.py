def gcd(num1, num2):
    array = [num1, num2]
    array.sort()
    while array[0] != array[1]:
        if array[0] <= 1 or array[1] <= 1: return 0
        diff = array[1] - array[0]
        array[1] = diff
        array.sort()
    return array[0]

def getTriple(k, m, n):
    a = k * ((m * m) - (n * n))
    b = k * (2 * m * n)
    c = k * ((m * m) + (n * n))
    return [a, b, c]

for a in range(1, 100):
    for b in range(1, 100):
        for c in range(1, 100):
            trip = getTriple(a, c, b)
            if trip[0] + trip[1] + trip[2] == 1000:
                if trip[0] > 0 and trip[1] > 0 and trip[2] > 0:
                    print("ANSWER!!!:", trip[0] * trip[1] * trip[2])
