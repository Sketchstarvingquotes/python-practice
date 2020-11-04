#Python sets

programs = {"java", "python", "c++", "html", "css", "javascript"}
print("Original set", programs)

for it in programs:
    print(it)


if "html" in programs:
    print("yes, 'html' is in programs")

WebDevelopment = {"html", "css", "react", "redux", "agile"}

#copy method 
cpy = programs.copy()
print(cpy)

#remove method 
cpy.remove("java")
print(cpy)

#pop method 
a = WebDevelopment.pop()
print(a)

#difference
WebDevelopment.difference(programs)
print(WebDevelopment)
#difference update 
programs.difference_update(WebDevelopment)
print(programs)

#symmatric difference
programs.symmetric_difference(WebDevelopment)
print(programs)

#intersection
WebDevelopment.intersection(programs)
print(WebDevelopment)

#intersection update
programs.intersection_update(WebDevelopment)
print(programs)

#isdisjoint
jnt = WebDevelopment.isdisjoint(programs)
print(jnt)

#issubset
subset = programs.issubset(WebDevelopment)
print(subset)

#union method 
programer = programs.union(WebDevelopment)
print(programer)

#update method 
programs.update(WebDevelopment)
print(programs)

#symmatric difference update
WebDevelopment.symmetric_difference_update(programs)
print(WebDevelopment)

#clear method 
clr = WebDevelopment.clear()
print(clr)

#discard method
card = WebDevelopment.discard("css")

#diffrence method
new = programs.difference(WebDevelopment)
print(new)




