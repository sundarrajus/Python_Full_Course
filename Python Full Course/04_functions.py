# ============================================================
# TOPIC: Functions — Basics, Return, Parameters
# ============================================================

def f():
    print('local')

f()


def s(num):
    print('hello')
    print(num)

s(20)


# ============================================================
# TOPIC: Functions — Global Variables
# ============================================================

var = 20

def k():
    global var
    var = 5
    print('hello')
    print(var)

k()
var = 25
var += 5
print(var)


# ============================================================
# TOPIC: Functions — Return Statement
# ============================================================

def f(n):
    if n % 2 == 0:
        return "even"
    return "odd"

print(f(8))


def f():
    if a > b and a > c:
        return "a is greater"
    elif b > c:
        return "b is greater"
    return "c is greater"

a, b, c = 23, 43, 35
print(f())


# ============================================================
# TOPIC: Functions — *args and **kwargs
# ============================================================

def g(*args):
    print(args)

g(2, 4, 5, 6)
g(5)


def g(**kwargs):
    print(kwargs)

g(a=2, b=4)
g(c=5)


# Default parameters
def g(a=20, b=5, c=9):
    print(a, b, c)

g(a=2, b=4)
g()
g(c=5)


# Keyword arguments
def g(a, b, c):
    print(a, b, c)

g(2, b=4, c=5)


# ============================================================
# TOPIC: Functions — Number Programs
# ============================================================

# Prime check
def prime(n):
    if n < 1:
        return 'not'
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return 'not'
    return 'prime'

print(prime(7))


# Sum of digits
def add(n):
    sum = 0
    while n > 0:
        rem = n % 10
        sum += rem
        n //= 10
    return sum

print(add(432))


# Armstrong number
def arm(n):
    sum = 0
    dup = n
    pow = len(str(n))
    while n > 0:
        rem = n % 10
        sum = sum + rem ** pow
        n //= 10
    return 'armstrong' if sum == dup else 'not'

print(arm(153))


# Reverse a number
def rev(n):
    sum = 0
    while n > 0:
        rem = n % 10
        sum = sum * 10 + rem
        n //= 10
    return sum

print(rev(12345))


# Integer to Binary
def itb(n):
    p = 1
    sum = 0
    while n > 0:
        rem = n % 2
        sum = sum + rem * p
        n //= 2
        p *= 10
    return sum

print(itb(8))


# Binary to Integer
def bti(n):
    sum = 0
    p = 0
    while n > 0:
        rem = n % 10
        sum = sum + rem * (2 ** p)
        p += 1
        n //= 10
    return sum

print(bti(1000))


# Factorial
def fact(n, fact=1):
    for i in range(1, n + 1):
        fact = fact * i
    return fact

print(fact(5))


# Strong number
def strong(n):
    sum = 0
    dup = n
    while n > 0:
        rem = n % 10
        fact = 1
        for i in range(1, rem + 1):
            fact *= i
        sum += fact
        n //= 10
    return 'strong' if sum == dup else 'not'

print(strong(145))


# ============================================================
# TOPIC: Functions — Happy Number
# ============================================================

def happy(n):
    while n > 9:
        sum = 0
        while n > 0:
            rem = n % 10
            sum = sum + rem * 2
            n //= 10
        n = sum
    return 'happy' if n == 1 or n == 7 else 'not'

print(happy(7))
