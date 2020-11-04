class parent:
    def get_name(self, name):
        self.name = name
    def show_name(self):
        return self.name 

class child(parent):
    def get_age(self, age):
        self.age = age
    def show_age(self):
        return self.age

class GandChild(child):
    def get_address(self, address):
        self.address = address 
    def show_address(self):
        return self.address

gc = GandChild()

gc.get_name("Parimal Raut")
gc.get_age(24)
gc.get_address("Near railway station Akola")

gc.show_name()
gc.show_age()
gc.show_address()
