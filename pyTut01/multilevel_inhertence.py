class Dad:
    basketball = 1
    pass

class Son(Dad):
    dance = 1
    basketball = 3
    def isdance(self):
        return f"Yes I dance {self.dance} no of times"
    pass
#override
class GrandSon(Son):
    dance = 6
    #copy method from son
    def isdance(self):
        return f"Yes I dance very awsomely {self.dance} no of times"


darry = Dad()
larry = Son()
harry = GrandSon()

print(harry.isdance())
print(harry.basketball)





