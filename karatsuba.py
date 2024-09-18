import sys
import random

#Fix Binary Operations
def addBinary(x,y):
    x,y = ajustSize(x,y)
    sum = ""
    carry = False
    for i in range(len(x) - 1, -1, -1):
        if x[i] == "0" and y[i] == "0":
            if carry:
                sum = "1" + sum
                carry = False
            else: sum = "0" + sum
        elif x[i] == "1" and y[i] == "1":
            if carry:
                sum = "1" + sum
            else: 
                carry = True
                sum = "0" + sum
        elif x[i] == "1" or y[i] == "1":
            if carry:
                sum = "0" + sum
            else: sum = "1" + sum
    if carry:
        sum = "1" + sum
    return sum
def multiplyBinary(x,y):
    if x == "0" or y == "0":
        return "0"
    else: return "1"
def substractBinary(x,y):
    x,y = ajustSize(x,y)
    sub = ""
    carry = False

    for i in range(len(x) - 1, -1, -1):
        if x[i] == "0" and y[i] == "0":
            if carry:
                sub = "1" + sub
            else: sub = "0" + sub
        elif x[i] == "1" and y[i] == "1":
            if carry:
                sub = "1" + sub
            else: 
                sub = "0" + sub
        elif x[i] == "1":
            if carry:
                carry = False
                sub = "0" + sub
            else: sub = "1" + sub
        elif x[i] == "0":
            if carry:
                sub = "0" + sub
            else: 
                carry = True
                sub = "1" + sub
    if carry:
        sub = "1" + sub
    return sub
def ajustSize(x,y):
    maxSize = max([len(x), len(y)])
    x = x.zfill(maxSize)
    y = y.zfill(maxSize)
    return [x,y]

def karatsuba(num1,num2):
    num1,num2 = ajustSize(num1,num2)
    if len(num1) == 1 or len(num2) == 1:
        return multiplyBinary(num1,num2)
    
    half = len(num1)//2
    secondhalf = len(num1) - half

    # Divide numbers in half
    a = num1[:half]
    b = num1[half:]
    c = num2[:half]
    d = num2[half:]
    
    # Call karatsuba recursively 3 times
    x = karatsuba(a,c)
    y = karatsuba(addBinary(a,b),addBinary(c,d))
    z = karatsuba(b,d)

    # Calculate the result
    y = substractBinary(y,x)
    y = substractBinary(y,z)
    
    for i in range(secondhalf):
        x = x + "00"
        y = y + "0"

    sum = addBinary(x,z)
    sum = addBinary(sum,y)

    sum = sum.lstrip('0')
    if sum == '':
        sum = '0'
    return sum

if len(sys.argv) != 3:
    print("Usage: python3 karatsuba.py <bin1> <bin2>")
    sys.exit(1)

#Get the two binary numbers
bin1 = sys.argv[1]
bin2 = sys.argv[2]

for i in range(len(bin1)):
    if bin1[i] != "0" and bin1[i] != "1":
        print("Error: The first binary number is not valid")
        sys.exit(1)
for i in range(len(bin2)):
    if bin2[i] != "0" and bin2[i] != "1":
        print("Error: The second binary number is not valid")
        sys.exit(1)

# Se their sizes and make them equal, adding 0s to the left
bin1, bin2 = ajustSize(bin1, bin2)

# Call karatsuba function
print(karatsuba(bin1, bin2))
