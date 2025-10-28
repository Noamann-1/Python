    
n=int(input("enter one number"))
n2=int(input("enter another number"))
s=min(n,n2)
for i in range(1,s+1):
    if(n%i==0 and n2%i==0):
        hcf=i
print(f"HCF of {n} and {n2} = {hcf}")
    