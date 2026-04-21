# ============================================================
# TOPIC: Recursion — Sum of Digits
# ============================================================

def Add(n):
    if n == 0:
        return 0
    return (n % 10) + Add(n // 10)

print(Add(456))


# ============================================================
# TOPIC: Recursion — Armstrong Number
# ============================================================

def s(n, p):
    if n == 0:
        return 0
    return (n % 10) ** p + s(n // 10, p)

n = 153
p = len(str(n))
if s(n, p) == n:
    print('arm')
else:
    print('not')


# ============================================================
# TOPIC: Recursion — Disarium Number
# ============================================================

def s(n, p):
    if n == 0:
        return 0
    return (n % 10) ** p + s(n // 10, p - 1)

n = 135
p = len(str(n))
if s(n, p) == n:
    print('disarm')
else:
    print('not')


# ============================================================
# TOPIC: Recursion — Factorial
# ============================================================

def f(n):
    if n == 0 or n == 1:
        return 1
    return n * f(n - 1)

print(f(4))


# ============================================================
# TOPIC: Recursion — Integer to Binary
# ============================================================

def s(n, p=1):
    if n == 0:
        return 0
    return (n % 2) * p + s(n // 2, p * 10)

print(s(8))


# ============================================================
# TOPIC: Recursion — Binary to Integer
# ============================================================

def s(n, p=0):
    if n == 0:
        return 0
    return (n % 10) * (2 ** p) + s(n // 10, p + 1)

print(s(1000))


# ============================================================
# TOPIC: Recursion — Reverse a Number
# ============================================================

def s(n, p):
    if n == 0:
        return 0
    return (n % 10) * p + s(n // 10, p // 10)

n = 456
p = 10 ** (len(str(n)) - 1)
print(s(n, p))


# ============================================================
# TOPIC: Recursion — Strong Number
# ============================================================

def f(n):
    if n < 0:
        return 'not'
    if n == 0 or n == 1:
        return 1
    return n * f(n - 1)

def s(n):
    if n == 0:
        return 0
    return f(n % 10) + s(n // 10)

n = 145
print('strong' if n == s(n) else 'not')


# ============================================================
# TOPIC: Recursion — Palindrome Prime (Pali-Prime)
# ============================================================

def p(n, v=1):
    if v == n + 1:
        return 0
    if n % v == 0:
        return 1 + p(n, v + 1)
    else:
        return 0 + p(n, v + 1)

def r(n, p):
    if n == 0:
        return 0
    return (n % 10) * p + r(n // 10, p // 10)

def pp(n):
    pow = 10 ** (len(str(n)) - 1)
    return 'palyprime' if (p(n) == 2 and r(n, pow) == n) else 'not'

n = 11
print(pp(n))


# ============================================================
# TOPIC: Recursion — EMIRP Number
# ============================================================

def p(n, v=1):
    if v == n + 1:
        return 0
    if n % v == 0:
        return 1 + p(n, v + 1)
    else:
        return 0 + p(n, v + 1)

def r(n, p):
    if n == 0:
        return 0
    return (n % 10) * p + r(n // 10, p // 10)

def emirp(n):
    pow = 10 ** (len(str(n)) - 1)
    return 'EMIRP' if (p(n) == 2 and r(n, pow) != n and p(r(n, pow)) == 2) else 'not'

n = 13
print(emirp(n))


# ============================================================
# TOPIC: Recursion — Happy Number
# ============================================================

def s(n):
    if n == 0:
        return 0
    return (n % 10) ** 2 + s(n // 10)

def h(n):
    if n > 9:
        n = s(n)
        return h(n)
    if n == 1 or n == 7:
        return 'happy'
    return 'not happy'

n = 13
print(h(n))
