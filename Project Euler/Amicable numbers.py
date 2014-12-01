def factorize(number):
    x = 1
    result = []
    while x * x <= number:
        if number % x == 0:
            result.append(x)
            if x * x != number and x != 1:
                result.append(int(number / x))
        x += 1
    result.sort()
    return result

def arraySum(array):
    count = 0
    for x in array:
        count += x
    return count

myList = []
for x in range(10000):
    y = arraySum(factorize(x))
    if x != y and arraySum(factorize(y)) == x:
        myList.append(x)

print(myList)
print(arraySum(myList))
