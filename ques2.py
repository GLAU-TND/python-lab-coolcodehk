#type error

try:
    a=5
    b='hk'
    c=a+b
except TypeError:
    print("Type Error")
else:
    print('sucessfull')

#value error

try:
    print(float('hk'))
except ValueError:
    print("value Error")
else:
    print('Sucess')

#atrribute Error

class Attributes(object):
    a=2

try:
    object=Attributes()
    print(object.attribute)
except AttributeError:
    print('Attribute Error')