import math
#floating error
a=1.2
b=1
x=a-b
print(x)
#scalling error
n1=1000000
n2=1
print(n1+n2-n1)
#rounding error 
print(0.1+0.2)
print(round((0.1+0.2),2))
#iteration
arr=[0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]
sum=0
for i in arr:
    sum+=i
print(sum)
#truncation
x=math.radians(90)
z=x-(x**3)/6
print(z)
print(math.sin(x))