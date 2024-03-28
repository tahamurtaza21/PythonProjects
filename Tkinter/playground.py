# for unlimited arguments
# the paramter name can be anything, but you need to add the asterisk
# Additionally it allows for an unlimited number of arguments

def add(*args):
    counter = 0
    for n in args:
        counter += n
    return counter

#add(1,3,4,5,346,345,3,64,64,64,64,646,46,46)

def calculate(n, **kwargs):
    print(kwargs)
    #for key, value in kwargs.items():
        #print(key)
        #print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2,add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        #self.make = kw["make"] will give error if doesn't exist
        #self.model = kw["model"]

        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make="Nissan")
print(my_car.model)

