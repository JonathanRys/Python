def factorsOf(num):
    i=1
    counter=0
    print('The factors of', num, 'are:')
    while i*i <= num:
        quotient=num/i
        compVal=int(quotient)
        if num%i in[0]: #quotient==compVal:
            print(i, '\t', compVal)
            counter=counter+1
        i=i+1
    if counter==1:print(num, 'is prime.\n')
    else:print(" ")
while True:
    dividend=input('Enter the number you want to find the factors of, or enter "x" to exit: ')
    if dividend=="x":break;
    try:
        factorsOf(int(dividend))
    except ValueError:
        print('Illegal value entered.\n')
