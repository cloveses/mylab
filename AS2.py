def binary_postive(x, length):
    lst=[]
    digit=0
    while(2**digit<x):
        digit=digit+1
    digit=digit+1
    num=2**(digit-1)
    for i in range(digit):
        if(x>=num and num>0):
            lst.append(1)
            x=x-num
            num=num//2
        if(x<num and num>0):
            num=num//2
            lst.append(0)
    if(length>digit):
        lst=[0]*(length-len(lst))+lst
    if(length<digit):
        lst=lst[-length:]
    return lst

def binary(x, length):
    if x >= 0:
        return binary_postive(x, length)
    else:
        lst = binary_postive(-x, length)
        lst[0] = 1
        return lst

def flip(a, length):
    for i in range(1,length):
        if a[i]==0:
            a[i]=1
        else :
            a[i]=0
    return a

def bit_add(first, second, i, carry):
    if (first[i]==0 and second[i]==0 and carry==0):
        return 0, 0
    elif (first[i]==1 and second[i]==0 and carry==0):
        return 1, 0
    elif (first[i]==0 and second[i]==1 and carry==0):
        return 1, 0
    elif (first[i]==0 and second[i]==0 and carry==1):
        return 1, 0
    elif (first[i]==1 and second[i]==1 and carry==0):
        return 0, 1
    elif (first[i]==1 and second[i]==0 and carry==1):
        return 0, 1
    elif (first[i]==0 and second[i]==1 and carry==1):
        return 0, 1
    elif (first[i]==1 and second[i]==1 and carry==1):
        return 1, 1

def twosComplementBinaryAddition(L1, L2):
    carry = 0
    res = [0,] * len(L2)
    carry = 0
    for i in range(len(L1)-1, -1, -1):
        total, carry = bit_add(L1, L2, i, carry)
        res[i] = total
    return res

def decimalToTwosComplement(num, length):
    lst = binary(num, length)
    if lst[0]:
        lst = flip(lst, len(lst))
        return twosComplementBinaryAddition(lst, [0,] *( len(lst)-1) + [1,])
    else:
        return lst


def twosComplementToDecimal(L3):
    positive = 1
    if L3[0]:
        L3 = flip(L3, len(L3))
        L3 = twosComplementBinaryAddition(L3, [0,] * (len(L3)-1) + [1,])
        positive = -1

    L3 = L3[1:]
    numbers = [2**i for i in range(len(L3))][::-1]
    numbers = [i*j for i,j in zip(numbers, L3)]
    return sum(numbers) * positive



if __name__ == '__main__':

    LENGTH = int(input("Please enter list length "))
    a = int(input("Enter a "))
    b = int(input("Enter b "))
    c = a + b
    L1 = decimalToTwosComplement(a, LENGTH)
    print "The two complement representation of", a, "is", L1
    L2 = decimalToTwosComplement(b, LENGTH)
    print "The two complement representation of", b, "is", L2
    L3 = twosComplementBinaryAddition(L1, L2)
    print "The two complement addition of", a, "and", b, "is", L3
    d = twosComplementToDecimal(L3)
    print "Converting the two complement to decimal gives", d
    if (c == d):
        print "Since", c, "==", d, ", it seems we did good job."
    else:
        print "Since", c, "!=", d, ", either of a, b, c must be outside of the range."



