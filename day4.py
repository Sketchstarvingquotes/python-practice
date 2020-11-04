#Tuples and their examples

LaptopManufacturer = ("lenovo", "dell", "Hp", "acer", "asus", "apple")
print("Original tuple", LaptopManufacturer)
print(len(LaptopManufacturer))

#if statement in tuple
if "dell" in LaptopManufacturer:
    print("yes, 'dell' is in the LaptopManufacture")

#looping in tuples
for d in LaptopManufacturer:
    print(d)

#count method
a = LaptopManufacturer.count("lenovo")
print(a)

#index Method 
b = LaptopManufacturer.index("acer")
print(b)

#copy method in tuple
c = tuple(LaptopManufacturer)
print(c)

#coversition of tuple
LaptopSupliers = list(LaptopManufacturer)
LaptopSupliers[2] = "samsung"
print(LaptopSupliers)

#Join tuple
student = ("sam", "jhon", "mandy", "kedar", "varry")
RollNo = (24, 56, 48, 17, 22)

newtuple = student + RollNo
print(newtuple)

#We can"t able to change tuple but we can delete it 
systems = ("lenovo", "dell", "Hp", "acer", "asus", "apple", "samsung", "vivo")
print("Original tuple", systems)
del systems
print(systems)





