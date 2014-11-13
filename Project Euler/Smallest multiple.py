i = 1

def checkNum(number):
    for i in range(1, 21):
        if number % i != 0:
            return False
    return True

while True:
    if checkNum(i):
        break
    i += 1
print(i)
    
