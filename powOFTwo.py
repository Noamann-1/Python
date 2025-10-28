n=int(input("Enter Number to check: "))
n2=int(input(f"Enter number {n} is power of : "))
def powOf2(n,n2):
    i=1
    count=1
    while(n2**i<=n):
        if n2**i==n:
           print(f"\n{n} is {n2} ^ {i}!!")
           return
        i=i+1
        
    print("not")
def recpow2(n,n2):
    if n==1:
        return True
    if n%n2!=0:
        return False
    res=recpow2(n/n2,n2)
    return res
print(recpow2(n,n2))
powOf2(n,n2)