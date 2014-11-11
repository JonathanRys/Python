def factorsOf(num):
    i=1
    counter=0
    print("The factors of "+str(num)+" are:")
    while i*i <= num:
        quotient=float(num/i)
        compareVal=int(quotient)
        if quotient==compareVal:
            print(str(i)+"\t"+str(compareVal))
            counter=counter+1
        i=i+1
    if counter==1:print(str(num)+" is prime.\n")
    else:print(" ")

while True:
    dividend=input('Enter the number you want to find the factors of, or enter "x" to exit: ')
    if dividend=="x":break;
    try:
        factorsOf(int(dividend))
    except ValueError:
        print("Illegal value entered.\n")
