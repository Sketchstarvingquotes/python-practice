#Python list Examples
mobiles_company = ["Lenovo", "Motrola", "LG", "Realme", "Gionee", "Samsung", "Lava", "Oppo", "Vivo"]
print(mobiles_company)

#Positive Indexing

print(mobiles_company[2]) 

#Range Of Positive Indexing

print(mobiles_company[1:6])
print(mobiles_company[3:7])
print(mobiles_company[:4])
print(mobiles_company[3:])
print(mobiles_company[::5])
#Negative Indexing

print(mobiles_company[-3])

#Range Of Negative Indexing

print(mobiles_company[-7:-1])
print(mobiles_company[-9:-4])
print(mobiles_company[:-5])
print(mobiles_company[-4:])
print(mobiles_company[::6])

#Change value By using othere

mobiles_company[4] = "Nokia"
print(mobiles_company)

mobiles_company[7] = "Spice"
print(mobiles_company)

#METHODS OF LIST WITH EXAMPLE

#1)Append
lst1 = ['sam', 'varry', 'kedi', 'mady', 'mukul'] 
lst1.append('Pady')
print("After append", lst1)

#2)Extend
lst2 = [15, 14, 52, 84, 10]
print("Before Extend", lst2)
lst2.extend([45, 76, 89, 102])
print("After Extend", lst2)

#3)Insert
lst3 = ["Lenovo", "Motrola", "LG", "Realme", "Gionee", "Samsung", "Lava", "Oppo", "Vivo"]
print("Before Insert value", lst3)
lst3.insert(7, "Micromax")
print(lst3)

#4)Copy
lst4 = ["Lenovo", "Motrola", "LG", "Realme", "Gionee", "Samsung", "Lava", "Oppo", "Vivo"]
a = lst4.copy()
print(a)

#5)Clear
lst5 = ["Lenovo", "Motrola", "LG", "Realme", "Gionee", "Samsung", "Lava", "Oppo", "Vivo"]
print("Before Clear", lst5)
lst5.clear()
print("After Clear", lst5)

#6)Remove
lst6 = ["Lenovo", "Motrola", "LG", "Realme", "Gionee", "Samsung", "Lava", "Oppo", "Vivo"]
print("Before remove", lst6)
lst6.remove("Lenovo")
print("After Remove", lst6)

#7)Reverse
lst7 = ["Lenovo", "Motrola", "LG", "Realme", "Gionee", "Samsung", "Lava", "Oppo", "Vivo"]
print("Before reverse", lst7)
lst7.reverse()
print("After Reverse", lst7)


#8)count
lst8 = ["Lenovo", "Motrola", "LG", "Lenovo", "Realme", "Lenovo", "Gionee", "Samsung", "Lava", "Oppo", "Vivo"]
print("Before count", lst8)
values = lst8.count("Lenovo")
print("After count", values)

#9)Index
lst9 = ["Lenovo", "Motrola", "LG", "Realme", "Gionee", "Samsung", "Lava", "Oppo", "Vivo"]
print("Before index", lst9)
IndexNum = lst9.index('Lava')
print("After index", IndexNum)

#Pop and Sort works only based on numaric values means, int,float,etc

#10)Pop
items = ["Lenovo", "Motrola", "LG", "Realme", "Gionee", "Samsung", "Lava", "Oppo", "Vivo"] 
print("Before pop", items)
items.pop()
print("After pop", items)

#11)Sort
numbers = [10, 15, 12, 56, 20, 52, 89, 74, 82, 45, 18, 17]
print("Before Sort", numbers)
numbers.sort()
print("After Sort", numbers)

#List also having dictionary examples are below

#1)Items
list = {1: "physics", 2: "chemistry", 3: "Mathematics", 4: "English", 5: "Biology"}
print("Original Dict:", list)
val = list.items()
print("After items", val)

#2)get
list1 = list.get(2)
print(list1)
#for replace value
list[2] = "Fishary"

#3)Values
list2 = list.values()
print(list2)
#it's shows all values from list or dictionary

#4)update
#it's shows latest update on list or dictionary
up = list.update()
print(up)

set = list.setdefault(3)
print(set)

#6)Key
list3 = {1:10, 2:15, 3:12, 4:56, 5:20, 6:52, 7:89, 8:74, 9:82, 10:45, 11:18, 12:17}
print(list3.keys())

#7)Popitems
list4 = {1:10, 2:15, 3:12, 4:56, 5:20, 6:52, 7:89, 8:74, 9:82, 10:45, 11:18, 12:17}
print("before popitem", list4)
list4.popitem()
print(list4)



