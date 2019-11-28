class Myexception(Exception):
    def __init__(self,v):
        self.v=v
        pass
    def __str__(self):
        print(self.v)




def add(a, b):
    c = a + b
    if c < 150:
        raise Myexception('Custom Excption Occured')
    else:
        return c

a=int(input())
b=int(input())
print(add(a,b))



