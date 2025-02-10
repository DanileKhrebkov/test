class Stack:
    def __init__(self):
        self.__stacklist = []

    def push(self, val):
        self.__stacklist.append(val)


    def pop(self):
        val = self.__stacklist[-1]
        del self.__stacklist[-1]
        return val

class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0
    def push(self, val):
        self.__sum += val
        Stack.push(self,val)