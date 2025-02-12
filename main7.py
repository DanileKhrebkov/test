class ExampleClass:
    def __init__(self, val = 1):
        self.first = val
    def setSecond(self, val):
        self.second = val


ExampleObject1 = ExampleClass()
ExampleObject2 = ExampleClass(2)
ExampleObject2.setSecond(3)
ExampleObject3 = ExampleClass(4)
ExampleObject3.third = 5
print(ExampleObject1.__dict__)
print(ExampleObject2.__dict__)
print(ExampleObject3.__dict__)