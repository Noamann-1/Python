
def binaryToDecimal(b):
    reversed_s = b[::-1]
    decimal = 0
    p = 0
    for i in reversed_s:
        if i == '1':      
            decimal += 2 ** p
        p += 1
    print(decimal)


n = int(input("Enter a decimal number: "))
def decimalToBinary(n):
    binary = ""
    while n > 0:
        binary = str(n % 2)+binary
        n //= 2
    return binary if binary != "" else "0"


print(decimalToBinary(n))
while(1):
   print("1 for Binary To Decimal:")
   print("2 for Decimal To Binary: ")
   print("3 for exit.")
   ch=int(input("enter choice"))
   if(ch==1):
       b = input("Enter binary code: ")
       binaryToDecimal(b)