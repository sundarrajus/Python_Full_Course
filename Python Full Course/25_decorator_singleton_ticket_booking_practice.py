# ============================================================
# CLEANED PYTHON FULL COURSE
# FILE: 25_decorator_singleton_ticket_booking_practice.py
# ============================================================

def SingleTon(arg):
    d={}
    def inner():
        if len(d)==0:
            ob=arg()
            d['a']=ob
        return d['a']                               #multiple Movies ticket booking
    return inner
@SingleTon
class Movie1:
    def __init__(self):
        self.maxtic=200
    def Booking(self):
        print(f'Available tickets : {self.maxtic}')
        count=int(input('enter no. of tickets :'))
        if 0<=count<=self.maxtic:
                  print('tickets booked successfully')
                  self.maxtic-=count
                  print(f'Remaining tickets :{self.maxtic}')
        else:
            print('no ticktes')
@SingleTon           
class Movie2:
    def __init__(self):
        self.maxtic=200
    def Booking(self):
        print(f'Available tickets : {self.maxtic}')
        count=int(input('enter no. of tickets :'))
        if 0<=count<=self.maxtic:
                  print('tickets booked successfully')
                  self.maxtic-=count
                  print(f'Remaining tickets :{self.maxtic}')
        else:
            print('no ticktes')
@SingleTon            
class Movie3:
    def __init__(self):
        self.maxtic=200
    def Booking(self):
        print(f'Available tickets : {self.maxtic}')
        count=int(input('enter no. of tickets :'))
        if 0<=count<=self.maxtic:
                  print('tickets booked successfully')
                  self.maxtic-=count
                  print(f'Remaining tickets :{self.maxtic}')
        else:
            print('no ticktes')

def bms():
    print('WELCOME TO BOOKMYSHOW')
    print('1=>Movie1\n2=>Movie2\n3=>Movie3')
    choice=int(input('enter your choice: '))
    if choice==1:
        obj=Movie1()
        obj.Booking()
    elif choice==2:
        obj=Movie2()
        obj.Booking()
    elif choice==3:
        obj=Movie3()
        obj.Booking()
    else:
        print('no movies')

def paytm():
    print('WELCOME TO PAYTM BOOKING')
    print('1=>Movie1\n2=>Movie2\n3=>Movie3')
    choice=int(input('enter your choice: '))
    if choice==1:
        obj=Movie1()
        obj.Booking()
    elif choice==2:
        obj=Movie2()
        obj.Booking()
    elif choice==3:
        obj=Movie3()
        obj.Booking()
    else:
        print('no movies')
        
bms()
paytm()