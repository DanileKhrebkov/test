class Exampleclass:
    __counter = 0
    def __init__(self, val = 1):
        self.__first =val
        Exampleclass.__counter +=1

exampleobject1 = Exampleclass()
exampleobject2 = Exampleclass(2)
exampleobject3 = Exampleclass(4)
print(exampleobject1.__dict__, exampleobject1._ExampleClass__counter)
print(exampleobject2.__dict__, exampleobject2._ExampleClass__counter)
print(exampleobject3.__dict__, exampleobject3._ExampleClass__counter) 