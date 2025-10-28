n=int(input("enter a number: "))
def fibonacci(num):
    if(num==0):
        return 0
    elif(num==1):
        return 1
    else:
        fib=[0]*n
        fib[0]=0
        fib[1]=1
    for i in range(2,n):
     fib[i]=fib[i-1]+fib[i-2]
    return fib
print(fibonacci(8))