# In python method overloading is not supports but same concept we can achieve using
#                               default arguments & variable arguments(*args)

"""             IN JAVA, it supports but not in python
                int add(a, b){ return a + b; }
                int add(a, b, c) {return a + b + c; }
                int add(a, b, c, d) { return a + b + c + d; }"""


# default arguments
class DefaultArgumentExample():

    # instead of multiple methods python use one methods handles multiple cases
    # c = 0 is default variable assignment
    def addition(self, a, b, c=0):
        return a + b + c

    # Error
    # def adding(self, a =10 , b =20, c=20):
    #     return a + b + c

add = DefaultArgumentExample()
print(add.addition(10,20,))
print(add.addition(5,20, 10))
print(add.addition(10, 20, 30))


#variable arguments(*args)
class VariableArgumentExample:

    # sum() in-build function
    def addition(self, *args):
        return sum(args)

    def nums(self, *args):
        print(args)

add = VariableArgumentExample()
print(add.addition(1,2,3,4,5))
print(add.addition(10,20,30,40,50))
print(add.addition(100,200,300))
add.nums(5,2,35)

#Mixing normal parameters with *args
class Welcome:

    def greet(self, message, *names):
        for name in names:
            print(f'{message} {name}')

greet1 = Welcome()
greet1.greet("Hello", "Jessy", "Mark", "Jorden")


#*args in real projects
class Order:

    def log(self,*messages):
        for msg in messages:
            print(msg)