class Myclass:
    classvar = "My class variable"
    @classmethod
    def classmethod(cls): #class method
        return cls.classvar
print(Myclass.classmethod())

