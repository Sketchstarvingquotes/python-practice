class student:
    def self_intro(self):
        print("my name is:" + self.name)
        print("my age is:" + self.age)
        print("my roll no. is:" + self.roll)   


s1 = student()

s1.name = "Sam"
s1.age = "24"
s1.roll = "R52"

s2 = student()

s2.name = "ram"
s2.age = "23"
s2.roll = "R68"

s1.self_intro()
print(end='\n')
s2.self_intro()

#Init method 

class college:
    def __init__(self, name, branch, year):
        self.name = name
        self.branch = branch
        self.year = year

    def intro(self):
        print("myname is:" + self.name)
        print("my branch is:" + self.branch)
        print("I'm in:" + self.year)

c1 = college("Raj varma", "Mechanical", "Final year")
c2 = college("vijay sharma", "Civil", "second year")

c1.intro()
print(end="\n")
c2.intro()

        