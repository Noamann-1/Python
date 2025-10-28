def productTwo(n1,n2):
    if n2==0 or n1==0:
        return 0
    else:
        return n1+productTwo(n1,n2-1)
num1=100
num2=200
print(productTwo(num1,num2))