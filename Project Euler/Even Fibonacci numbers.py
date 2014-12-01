val = 1
oldval = 1
newval = 0
total = 0

while val < 4000000:
    newval = oldval + val
    oldval = val
    if val % 2 == 0:
        total += val
    val = newval
print(total)
