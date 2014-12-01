def getValue(string):
    retVal = 0
    for x in string:
        retVal += ord(x) - 64
    return retVal

f = open('p022_names.txt', 'r')
names = f.read().split('","')

names[0] = names[0][1:]
names[-1] = names[-1][0:-1]

f.close()
names.sort()

counter = 1
total = 0
for x in names:
    total += getValue(x) * counter
    counter += 1
print(total)

