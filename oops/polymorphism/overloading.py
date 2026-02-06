# In python method overloading is not supports but same concept we can achieve using
#                               default arguments & variable arguments(*args)

"""             IN JAVA it supports but not in python
                int add(a, b){ return a + b; }
                int add(a, b, c) {return a + b + c; }
                int add(a, b, c, d) { return a + b + c + d; }"""


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