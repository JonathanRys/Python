oneToTwenty = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
               'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
               'sixteen', 'seventeen', 'eighteen', 'nineteen']
ones = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
hundred = ['hundred']
thousand = ['thousand']

def strLen(array):
    arrayLen = 0
    for x in array:
        arrayLen += len(x)
    return arrayLen

total = 0
alpha =[]
for x in oneToTwenty:
    alpha.append(x)
    total += len(x)
dime = 0
for x in tens:
    alpha.append(x)
    dime += len(x)
    for y in ones:
        alpha.append(x + y)
        dime += len(x) + len(y)

total += dime
hundo = 0
for x in ones:
    alpha.append(x + hundred[0])
    hundo += len(x + hundred[0])
    for y in oneToTwenty:
        alpha.append(x + hundred[0] + 'and' + y)
        hundo += len(x + hundred[0]) + len('and' + y)      
    for y in tens:
        alpha.append(x + hundred[0] + 'and' + y)
        hundo += len(x + hundred[0]) + len('and' + y)
        for z in ones:
            alpha.append(x + hundred[0] + 'and' + y + z)
            hundo += len(x + hundred[0]) + len('and' + y) + len(z)

total += hundo
alpha.append(ones[0] + thousand[0])
gunit = (len(ones[0] + thousand[0]))
total += gunit

print('\n========\nTotal:        ', total)

