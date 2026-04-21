# ============================================================
# TOPIC: Decorators — Basics
# ============================================================

def outer(arg):
    def inner():
        arg()
    return inner

@outer
def sample():
    print('hello')

sample()


# ============================================================
# TOPIC: Decorators — With Arguments (Absolute Value)
# ============================================================

def outer(arg):
    def inner(a, b):
        if a < 0 and b < 0:
            a = a * (-1)
            b = b * (-1)
        elif a < 0:
            a = a * (-1)
        elif b < 0:
            b = b * (-1)
        arg(a, b)
    return inner

@outer
def add(a, b):
    print(a + b)

add(-4, 2)


# ============================================================
# TOPIC: Decorators — Division with Zero Handling
# ============================================================

def outer(arg):
    def inner(a, b):
        if a == 0 and b == 0:
            return 'not possible'
        elif b == 0:
            a, b = b, a
        return arg(a, b)
    return inner

@outer
def div(a, b):
    return a / b

print(div(0, 0))


# ============================================================
# TOPIC: Decorators — Singleton Pattern
# ============================================================

def outer(arg):
    l = []
    def inner():
        if len(l) == 0:
            obj = arg()
            l.append(obj)
        return l[0]
    return inner

@outer
class sample:
    def __init__(self):
        print('hello')

obj1 = sample()
obj2 = sample()
obj3 = sample()
print(obj1 is obj2 is obj3)    # True — all same object


# ============================================================
# TOPIC: Decorators — Singleton Movie Ticket Booking (Single Movie)
# ============================================================

def SingleTon(arg):
    l = []
    def inner():
        if len(l) == 0:
            ob = arg()
            l.append(ob)
        return l[0]
    return inner

@SingleTon
class Booking:
    def __init__(self):
        self.maxtic = 200

    def Movie(self):
        print(f'Available tickets : {self.maxtic}')
        count = int(input('enter no. of tickets: '))
        if 0 <= count <= self.maxtic:
            print('tickets booked successfully')
            self.maxtic -= count
        else:
            print('no tickets')

def bms():
    obj = Booking()
    obj.Movie()

bms()
bms()


# ============================================================
# TOPIC: Decorators — Singleton Multiple Movies Ticket Booking
# ============================================================

def SingleTon(arg):
    d = {}
    def inner():
        if len(d) == 0:
            ob = arg()
            d['a'] = ob
        return d['a']
    return inner

@SingleTon
class Movie1:
    def __init__(self):
        self.maxtic = 200

    def Booking(self):
        print(f'Available tickets : {self.maxtic}')
        count = int(input('enter no. of tickets: '))
        if 0 <= count <= self.maxtic:
            print('tickets booked successfully')
            self.maxtic -= count
            print(f'Remaining tickets : {self.maxtic}')
        else:
            print('no tickets')

@SingleTon
class Movie2:
    def __init__(self):
        self.maxtic = 200

    def Booking(self):
        print(f'Available tickets : {self.maxtic}')
        count = int(input('enter no. of tickets: '))
        if 0 <= count <= self.maxtic:
            print('tickets booked successfully')
            self.maxtic -= count
            print(f'Remaining tickets : {self.maxtic}')
        else:
            print('no tickets')

@SingleTon
class Movie3:
    def __init__(self):
        self.maxtic = 200

    def Booking(self):
        print(f'Available tickets : {self.maxtic}')
        count = int(input('enter no. of tickets: '))
        if 0 <= count <= self.maxtic:
            print('tickets booked successfully')
            self.maxtic -= count
            print(f'Remaining tickets : {self.maxtic}')
        else:
            print('no tickets')

def bms():
    print('WELCOME TO BOOKMYSHOW')
    print('1 => Movie1\n2 => Movie2\n3 => Movie3')
    choice = int(input('enter your choice: '))
    if choice == 1:
        obj = Movie1()
        obj.Booking()
    elif choice == 2:
        obj = Movie2()
        obj.Booking()
    elif choice == 3:
        obj = Movie3()
        obj.Booking()
    else:
        print('no movies')

def paytm():
    print('WELCOME TO PAYTM BOOKING')
    print('1 => Movie1\n2 => Movie2\n3 => Movie3')
    choice = int(input('enter your choice: '))
    if choice == 1:
        obj = Movie1()
        obj.Booking()
    elif choice == 2:
        obj = Movie2()
        obj.Booking()
    elif choice == 3:
        obj = Movie3()
        obj.Booking()
    else:
        print('no movies')

bms()
paytm()


# ============================================================
# TOPIC: Polymorphism — Method Overloading (using *args)
# ============================================================

class A:
    def a(self, *args):
        if len(args) == 0:
            return 0
        else:
            ans = 1
            for ele in args:
                ans *= ele
            return ans

obj = A()
print(obj.a(3, 3))
print(obj.a(3, 3, 9))
print(obj.a())


# ============================================================
# TOPIC: Polymorphism — Method Overriding
# ============================================================

class A:
    def m1(self):
        print('hi')

    def m2(self):
        print('hello')

class B(A):
    def m1(self):
        print('hiiiii')    # overrides A.m1

    def m2(self):
        print('hello00000')

obj = B()
obj.m1()


# ============================================================
# TOPIC: Abstraction — Abstract Class and Abstract Method
# ============================================================

from abc import ABC, abstractmethod

class mother(ABC):
    @abstractmethod
    def care(self):
        pass

    def money(self):
        print('money')

    def food(self):
        print('food')

class A(mother):
    def care(self):
        print('high')

class B(mother):
    def care(self):
        print('very high')

obj = B()
obj.care()
obj.money()
obj.food()
