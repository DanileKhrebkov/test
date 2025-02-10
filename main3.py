class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    


    def greet(self):
        print(f'Привет, я {self.name} и мне {self.age} лет')
createhumanobject = Human('Danil', 15)
createhumanobject.greet()