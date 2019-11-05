def binary(x,length):
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
            num=num/2
        if(x<num and num>0):
            lst.append(0)
            num=num/2
    if(length>digit):
        lst=[0]*(length-len(lst)+lst)
    if(length<digit):
        lst=lst[-length]
    return lst

def flip(lst, length):
    for i in range(length):
        if a[i]==0:
            a[i]=1
        else :
            a[i]=0
    return a[i]

def add(lst):
    if (first[i]==0 and second[i]==0 and carry==0):
        lst.append(0)
        carry=0
    elif (first[i]==1 and second[i]==0 and carry==0):
        lst.append(1)
        carry==0
    elif (first[i]==0 and second[i]==1 and carry==0):
        lst.append(1)
        carry==0
    elif (first[i]==0 and second[i]==0 and carry==1):
        lst.append(1)
        carry==0
    elif (first[i]==1 and second[i]==1 and carry==0):
        lst.append(0)
        carry==1
    elif (first[i]==1 and second[i]==0 and carry==1):
        lst.append(0)
        carry==1
    elif (first[i]==0 and second[i]==1 and carry==1):
        lst.append(0)
        carry==1
    elif (first[i]==1 and second[i]==1 and carry==1):
        lst.append(1)
        carry==1
    return add(lst,1)

def scomp(num, length):
    model = 2**length
    res = model + num
    return bin(res)[-length:]

# # Main Program
# LENGTH = int(input("Please enter list length "))
# a = int(input("Enter a "))
# b = int(input("Enter b "))
# c = a + b
# L1 = decimalToTwosComplement(a, LENGTH)
# print "The two complement representation of", a, "is", L1
# L2 = decimalToTwosComplement(b, LENGTH)
# print "The two complement representation of", b, "is", L2
# L3 = twosComplementBinaryAddition(L1, L2)
# print "The two complement addition of", a, "and", b, "is", L3
# d = twosComplementToDecimal(L3)
# print "Converting the two complement to decimal gives", d
# if (c == d):
#     print "Since", c, "==", d, ", it seems we did good job."
# else:
#     print "Since", c, "!=", d, ", either of a, b, c must be outside of the range."

if __name__ == '__main__':
    print(scomp(9, 8))
    print(scomp(-9, 8))
    print(scomp(128, 8))
