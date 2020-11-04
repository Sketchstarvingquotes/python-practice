#single level inheritanc
class employee:
    def __init__(self, empname, empid):
        self.empname = empname
        self.empid = empid

    def show_details(self):
        print("I'm a employee of cisco")
        print("My name is", self.empname)
        print("my id is", self.empid)

E = employee("Raghu", 546)
E.show_details()

class company(employee):
    def show_e(self):
        print("I'm a sineour employee of cisco")

C = company("Rajiv", 15)
C.show_details()

C.show_e()