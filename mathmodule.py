from math import *

a = int(input("enter number = "))
s = sqrt(a)
print("square root =", s)

v = floor(145.25)
print(v)

print(ceil(155.6))
print(fabs(-14))
print(exp(13))
print(end = "\n")


#trignomentry functions
print(cos(5))
print(sin(15))
print(tan(20))
print(log(16))
print(log10(10))
print(end = "\n")

#callable objects type methods
r = float(input("Enter radius of circle ="))
ar = pi*r*r
print("Area of circle =", ar)

y = int(input("Enter value ="))
f = e**(2*y)
print("e raised to power 2y =", f)

#built in functions
div = divmod(25, 27)
print(div)

lst = [25, 158, 247, 123, 245, 102, 78]
print(max(lst))
print(min(lst))
print(sum(lst))
print(end = "\n")

#logical conversion
print(oct(89))
print(bin(24))
print(hex(156))
print(end ="\n")
#pow, gcd 
A = 10
B = 12
print(pow(B, A))
print(gcd(A, B))