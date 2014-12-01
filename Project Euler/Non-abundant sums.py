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

abundants = []
for x in range(28123):
    if arraySum(factorize(x)) > x:
        abundants.append(x)
abundants = set(abundants)

myList = set(range(1, 28124))
for x in abundants:
    if x + x > 28124: break
    for y in abundants:
        total = (x + y)
        if total > 28124: break
        if total in myList:
            myList.remove(total)

print(arraySum(myList))
