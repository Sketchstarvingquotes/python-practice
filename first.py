class laptop:
    


    def config(self):
        print("i5, 2gb ram, 4gb graphics, HD1tb, 7th genration")


lp1 = laptop()
print(type(lp1))

lp2 = laptop()

lp1.config()
lp2.config()

#how to find id
l1 = laptop
l2 = laptop

print(id(l1))
print(id(l2))

