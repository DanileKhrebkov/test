class ExampleClass:
    def __init__(self, val = 1):
        self.first = val


    def setSecond(self, val = 2):
        self.second = val


ExampleObject1 = ExampleClass()
ExampleObject2 = ExampleClass(2)
ExampleObject2.setSecond(4)
ExampleObject3 = ExampleClass(4)
ExampleObject3.__third = 5

print(ExampleObject1.__dict__)
print(ExampleObject2.__dict__)
print(ExampleObject3.__dict__)
    