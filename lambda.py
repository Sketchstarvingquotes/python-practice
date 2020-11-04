#ananymous function
x = lambda a: a*a
print(x(3))

val = lambda n: n*n
print(val(2))

#lambda function  within user defined function

def A(v):
    return lambda h: h+v
    t = A(5)
    print(t(9)

#lambda within map function
l1 = [12, 25, 45, 57, 89, 25]
l2 = [32, 25, 57, 89, 24, 89, 56, 27]
l3 = list(map(lambda a,b: a*b, l1, l2))
print(l3)

#lambda within filter function
mylist = [12, 6, 8, 8, 5, 15, 56, 87]

newlist = list(filter(lambda r: (r/3 == 4) , mylist))

print(newlist)