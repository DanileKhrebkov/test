# class ExampleClass:
#     variable = 1
#     def __init__(self, val):
#         ExampleClass.variable = val

# print(ExampleClass.__dict__)
# ExampleObject1 = ExampleClass(154)
# ExampleObject2 = ExampleClass(90)
# ExampleObject3 = ExampleClass(999)
# print(ExampleClass.__dict__)





# class ExampleClass:
#     def __init__(self, val):
#         if val % 2 !=0:
#             self.a = 1
#         else:
#             self.b = 1 

# exampleObject=ExampleClass(1)

# print(exampleObject.a)

# if hasattr(exampleObject, 'b'):
#     print(exampleObject.b)






# class ExampleClass:
#     a=1
#     def __init__(self):
#         self.b=2

# ExampleObject = ExampleClass()
# print(hasattr(ExampleObject, 'a'))
# print(hasattr(ExampleObject, 'b'))
# print(hasattr(ExampleClass, 'b'))
# print(hasattr(ExampleClass, 'a'))





# class ExampleClass:
#     def method(self, par):
#         print(f'method {par}')

# abc = ExampleClass()
# abc.method(1)
# abc.method(2)
# abc.method(3)






# class ExampleClass:
#     def other(self):
#         print('other')

#     def method(self):
#         print('method')
#         self.other()

# obj = ExampleClass()
# obj.method()





# class Server:
#     def __init__(self, port, ip):
#         self.__port = port
#         self.__ip = ip

# myServer = Server(279015854, 1111.11)





class ExampleClass:
    def vis(self):
        print('visible')
    def __hidden(self):
        print('hidden')

obj = ExampleClass()
obj.vis()
try:
    obj.__hidden()
except:
    print('я нэ можу')

obj._ExampleClass__hidden()