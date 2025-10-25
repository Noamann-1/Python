def armstrongNum():
    n=int(input("Enter a number to check: "))
    num=n
    count=len(str(n))
    total=0
    while n>0:
        r=n % 10
        total+=r**count
        n//=10

    if total==num:
        print("Armstrong")
    else:
        print("Not Armstrong")
armstrongNum()