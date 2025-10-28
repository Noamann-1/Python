num = int(input("Enter a number: "))
def nPn(n):
    if n==1:
        print(f"{n} ** {n} = {n*n}")
        return n*n

    else:
        print(f"{n}**{n}={n*n}")
        return (n*n)+nPn(n-1)
print(nPn(num))