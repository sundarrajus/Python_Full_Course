# ============================================================
# TOPIC: OOP — Bank Project (Basic)
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
