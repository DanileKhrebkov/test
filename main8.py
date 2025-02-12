class ExampleClass:
    def __init__(self, val):
        self.first = val


    def sum(self, val):
        self.second = val
        return self.first + self.second
    
exampleObject = ExampleClass(5)
print(exampleObject.sum(9))