from array import*

a = array('i', [5, 10, 15, 20, 25, 85, 76])
print(a)
print(a.buffer_info()) #buffer info shows size of array

#for loop through array
print("a values")
for x in a:
    print(x)

#while loop through array
i = 0
while i < len(a):
    print('\n')
    print(a[i])
    i = i+1

b= a[3]
print(b)

c = len(a)
print(c)

a.append(75)
print(a)

a.extend([3, 29])
print(a)

a.insert(45, 59)
print(a)

a.pop()
print(a)

a.remove(25)
print(a)

#slicing Array
print(a[0:4])
print(a[0:2])

#concatination
a2 = array("i", [782, 587, 214, 47852, 214, 231, 562])
new = array("i")
new = a + a2
print(new) #it's attach the values of a2 on the last of the a