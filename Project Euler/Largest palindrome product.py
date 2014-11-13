x = 100
y = 1000
result = 0
def isPalindrome(number):
    length = len(number)
    left = number[0:length//2]
    right = number[length//2: len(number)]
    if left == right[::-1]:
        return True

for n in range(x,y):
    for m in range(x,y):
        product = m * n
        if isPalindrome(str(product)) and result < product:
            result = product
            

print(result)
