class Dog(object):
    cry = "bark"
    def __init__(self,name):
        self.name = name

    def greeting(self):
        print ("i am " + self.name + "and I love to" + self.cry)

class Retriever(Dog):
    pass

class Golden(Retriever):
    def greeting(self):
        return "OHAI!" + str(Retriever.greeting(self))

Sydney = Golden("Sydney")
Sydney.greeting()


# important the code snippet is used only when the subclasses dont have __init__ of their own and thus check when instanciated for the __init__ of the 
# when the and __init__ is not found it uses that of the superclass
# else it uses its own, which can eventually be binded to the super using super(sub_classname, self).method or attribute
# multiple inheritance
# method resolution order can be checked  using class.__mro__
# by simply aranging the signature of the class properly e.d class victor(justice, mercy)
# hence if there is a method common to both justice and mercy python calls justice first



        
        