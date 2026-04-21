# ============================================================
# TOPIC: OOP — Encapsulation (Public, Protected, Private)
# ============================================================

class sample:
    a = 1
    def __init__(self):
        self._a = 10    # protected

    def m1(self):
        print(self.a)

obj1 = sample()
obj1.m1()
print(obj1._a)


class sample:
    a = 1
    def __init__(self):
        self.__a = 10   # private

    def getter(self):
        return self.__a

    def setter(self):
        self.__a = 30

obj1 = sample()
print(obj1.getter())
obj1.setter()
print(obj1.getter())


class bank:
    def __init__(self, pin, bal):
        self._pin = pin     # protected
        self.__bal = bal    # private

    def m1(self, pin):
        if pin == self._pin:
            return self.__bal
        return 'wrong'

obj1 = bank(11, 3456)
print(obj1.m1(11))


# ============================================================
# TOPIC: Inheritance — Single Level
# ============================================================

class A:
    a = 1
    b = 2

class B(A):
    c = 3
    d = 4

obj1 = B()
print(obj1.a)    # inherited from A


# ============================================================
# TOPIC: Inheritance — Method Chaining (super() and class ref)
# ============================================================

class A:
    def m1(self):
        print('m1 of class A')

    def m2(self):
        print('m2 of class A')

class B(A):
    def m1(self):
        print('m1 of class B')
        super().m1()     # super() chaining
        A.m1(self)       # class reference chaining

    def m2(self):
        print('m2 of class B')
        A.m2(self)

obj = B()
obj.m1()
obj.m2()


# ============================================================
# TOPIC: Inheritance — Multilevel
# ============================================================

class A:
    def __init__(self, messages, calls):
        self.messages = messages
        self.calls = calls

    def m1(self):
        print(self.messages)
        print(self.calls)

class B(A):
    def __init__(self, messages, calls, video, status):
        super().__init__(messages, calls)
        self.video = video
        self.status = status

    def m1(self):
        A.m1(self)
        print(self.video)
        print(self.status)

class C(B):
    def __init__(self, messages, calls, video, status, payment, channels):
        B.__init__(self, messages, calls, video, status)
        self.payment = payment
        self.channels = channels

    def m1(self):
        B.m1(self)
        print(self.payment)
        print(self.channels)

class D(C):
    def __init__(self, messages, calls, video, status, payment, channels, stickers, emojis):
        C.__init__(self, messages, calls, video, status, payment, channels)
        self.stickers = stickers
        self.emojis = emojis

    def m1(self):
        C.m1(self)
        print(self.stickers)
        print(self.emojis)

obj1 = D('hi', 'possible', 'available', 'good morning', 'no money', 'pyspiders', 'funny', ':)')
obj1.m1()


# ============================================================
# TOPIC: Inheritance — Multiple Inheritance
# ============================================================

class A:
    a = 1
    def d(self):
        self.bal += 500

class B:
    def d(self):
        self.bal += 500

class C(A, B):
    def __init__(self, bal):
        self.bal = bal

    def d(self):
        super().d()    # calls A.d() via MRO
        B.d(self)
        print(self.bal)

obj = C(1000)
obj.d()


# ============================================================
# TOPIC: Inheritance — Hierarchical
# ============================================================

class A:
    a = 10
    b = 20

class B(A):
    a = 8
    c = 8

class C(A):
    d = 9
    b = 8

obj = C()
print(obj.a)    # 10 (from A, C doesn't override 'a')


# ============================================================
# TOPIC: Inheritance — MRO (Method Resolution Order)
# ============================================================

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):    # Hybrid / Diamond inheritance
    pass

print(D.mro())
