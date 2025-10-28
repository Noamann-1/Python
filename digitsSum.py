n=int(input("enter a number:"))
def digSum(num):
    if(num==0):
     return 0
    return (num%10)+(digSum(num//10))
print(digSum(n))