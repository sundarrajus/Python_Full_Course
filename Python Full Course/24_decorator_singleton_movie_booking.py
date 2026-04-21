# ============================================================
# CLEANED PYTHON FULL COURSE
# FILE: 24_decorator_singleton_movie_booking.py
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
class Avengers:
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
            print('no tickets')

@SingleTon           
class TheDarkKnight:
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
            print('no tickets')

@SingleTon            
class TheyCallHimOG:
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
            print('no tickets')

def bms():
    print('WELCOME TO BOOKMYSHOW')
    print('1 => Avengers')
    print('2 => The Dark Knight')
    print('3 => They Call Him OG')
    choice=int(input('enter your choice: '))
    if choice==1:
        obj=Avengers()
        obj.Booking()
    elif choice==2:
        obj=TheDarkKnight()
        obj.Booking()
    elif choice==3:
        obj=TheyCallHimOG()
        obj.Booking()
    else:
        print('no movies')

def paytm():
    print('WELCOME TO PAYTM BOOKING')
    print('1 => Avengers')
    print('2 => The Dark Knight')
    print('3 => They Call Him OG')
    choice=int(input('enter your choice: '))
    if choice==1:
        obj=Avengers()
        obj.Booking()
    elif choice==2:
        obj=TheDarkKnight()
        obj.Booking()
    elif choice==3:
        obj=TheyCallHimOG()
        obj.Booking()
    else:
        print('no movies')

bms()
paytm()