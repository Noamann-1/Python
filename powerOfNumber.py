num1=int(input("Enter the number:"))
num2=int(input("Enter the power:"))
def power(n,m):
    if m==0:
        return 1
    else:
        return n*(power(n,m-1))
print(f"{num1} raised to power {num2} = {power(num1,num2)}")