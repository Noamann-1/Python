num=int(input("enter a number limit"))
x=0
for i in range(2,num+1):
    isPrime=True
    for x in range(2,num):
        if(x%i==0):
            isPrime=False

    print(x)