str = "sumit sudalkar"
print(str.capitalize())

str1 = "PYTHON NEED MORE PRACTICE"
a = str1.casefold()
print(a)

str2 = "It is example of count, count the number of string"
b = str2.count("count")
print(b)

str3 = "Align"
c = str3.center(30)
print(c)

str4 = "Working on Python"
x = str4.encode()
print(x)

str5 = "It is example of Encode"
d = str5.encode()
print(d)

str6 = "This is a endswith method."
e = str6.endswith(".")
print(e) 

str7 = "Hello, it's a practice"
f = str7.find("practice")
print(f)

str8 = "I am selling fruits in {price:.2f} rupees"
print(str8.format(price = 50))

str9 = "todays fruit sell 50kg"
g = str8.isdigit()
print(g)

str10 = "Demo String"
h = str10.isidentifier()
print(h)

str11 = "strin is in lowercase"
i = str11.islower()
print(i)

str12 = "72765464344"
j = str12.isnumeric()
print(j)

str13 = "When string have symbols like #? it is not printable, it it shows false"
k = str13.isprintable()
print(k)

str14 = "string having "  " whitespace"
l = str14.isspace()
print(l)

str15 = "Text Have Title Text"
m = str15.istitle()
print(m)

str16 = "SUPPER MEANS ALL TEXT IN UPERCASE FORMAT"
n = str16.isupper()
print(n)

str17 = ("bhole", "vishwa", "raghu")
o = "nath!".join(str17)
print(o)

str18 = "Python"
p = str18.ljust(1)
print(p, "need more practice")

str19 = "LOWER ALL TEXT"
q = str19.lower()
print(q)

str20 = "Python"
r = str20.lstrip()
print("of all programming language", r, "is my favorite")

str21 = "convert all string in uppercase"
s = str21.upper()
print(s)

str22 = "similar as a capitalize method"
t = str22.title()
print(t)

str23 = "charactersisinalphabets"
u = str23.isalpha()
print(u)

str24 = "Welcome to the python class"
v = str24.split()
print(v)

str25 = "150"
w = str25.zfill(5)
print(w)

str26 = "Hi, my name is sumit"
x = str26.startswith("Hi")
print(x)

str27 = {104: 72};
y = "hello sir";
print(y.translate(str27));

str28 = "Small Text in Capital and Capital Text In Small"
z = str28.swapcase()
print(z)