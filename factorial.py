n=int(input("Enter a number: "))
def factorial(num,a):
    if(num<1):
        return a
    return(factorial(num-1,num*a))
print(f"factorial of {n}={factorial(n,1)}")
