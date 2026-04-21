# ============================================================
# TOPIC: OOP — Class Variables vs Instance Variables
# ============================================================

class Animal:
    eyes = 2
    legs = 4

dog = Animal()
cat = Animal()
dog.legs = 3
Animal.legs = 5
print(dog.legs)      # 3 (instance overrides)
print(cat.legs)      # 5 (class variable)
print(Animal.legs)   # 5


# ============================================================
# TOPIC: OOP — Constructor (__init__)
# ============================================================

class Bank:
    IFSC = 'BANK420'
    B_LOC = 'Marathahalli'
    B_NAME = 'SBI'

    def __init__(self, name, acc_no, phone_no, aadhar, bal):
        self.name = name
        self.acc_no = acc_no
        self.phone_no = phone_no
        self.aadhar = aadhar
        self.bal = bal

obj1 = Bank('sundar', 2345678, 98765432, 2345678, 87)
obj1.bal = 50000
print(obj1.name, obj1.acc_no, obj1.bal)


# ============================================================
# TOPIC: OOP — Object Methods
# ============================================================

class sample:
    a = 10
    b = 100

    def __init__(self, c, d):
        self.c = c
        self.d = d

    def m1(self):
        print('hello')
        self.c = 45678    # modifying via obj reference

obj1 = sample(20, 30)
print(obj1.c)      # 20
obj1.m1()          # object reference call
print(obj1.c)      # 45678
sample.m1(obj1)    # class reference call


# ============================================================
# TOPIC: OOP — Class Method (@classmethod)
# ============================================================

class sample:
    a = 2
    b = 1

    def __init__(self, c, d):
        self.c = c
        self.d = d

    @classmethod
    def m1(cls):
        print('hello')
        cls.a = 45678
        print(cls)

obj1 = sample(4, 5)
obj1.m1()
print(obj1.a)
sample.m1()


# ============================================================
# TOPIC: OOP — Static Method (@staticmethod)
# ============================================================

class sample:
    a = 2
    b = 1

    def __init__(self, c, d):
        self.c = c
        self.d = d

    @staticmethod
    def m1():
        print('hello')

obj1 = sample(4, 5)
obj1.m1()
sample.m1()


# ============================================================
# TOPIC: OOP — Bank System (Object + Class + Static Methods)
# ============================================================

class Bank:
    IFSC = 'BANK420'
    B_LOC = 'Marathahalli'
    B_NAME = 'SBI'

    def __init__(self, name, acc_no, mobile, aadhar, password, bal):
        self.name = name
        self.acc_no = acc_no
        self.mobile = mobile
        self.aadhar = aadhar
        self.password = password
        self.bal = bal

    def check_bal(self):
        count = 3
        while count > 0:
            print(f'Number of attempts : {count}')
            if self.Getpin() == self.password:
                print(f'Available balance is : {self.bal}')
                break
            else:
                print('wrong pin...')
                count -= 1
        else:
            print('try after 24 hours later')

    def Deposit(self):
        amount = int(input('enter the amount to deposit : '))
        count = 3
        while count > 0:
            print(f'Number of attempts : {count}')
            if self.Getpin() == self.password:
                if 500 <= amount <= 10000:
                    if amount % 100 == 0:
                        self.bal += amount
                        print('Amount credited successfully...')
                        print(f'updated amount is : {self.bal}')
                        break
                    else:
                        print('Invalid denominations')
                else:
                    print('Invalid Amount')
            else:
                print('wrong pin...')
                count -= 1
        else:
            print('try again 24 hours later')

    def Withdraw(self):
        amount = int(input('enter the amount to withdraw : '))
        count = 3
        while count > 0:
            if self.Getpin() == self.password:
                if 500 <= amount <= 10000:
                    if amount % 100 == 0:
                        self.bal -= amount
                        print('Amount debited successfully...')
                        print(f'Available balance is : {self.bal}')
                        break
                    else:
                        print('Invalid denominations')
                else:
                    print('Invalid Amount')
            else:
                print('wrong pin...')
                count -= 1
        else:
            print('Try again 24 hours later')

    @classmethod
    def change_IFSC(cls):
        cls.IFSC = 'BANK1234'

    @staticmethod
    def Getpin():
        pin = int(input('enter your pin : '))
        return pin


obj1 = Bank('sundar', 45678, 9876543210, 234567890, 1234, 87654)
obj2 = Bank('Raju', 567, 543234, 65432234, 1111, 345)

obj1.Withdraw()
obj1.check_bal()
obj2.Deposit()
