# ============================================================
# TOPIC: filter() — Even Numbers
# ============================================================

def a(n):
    if n % 2 == 0:
        return True
    return False

print(list(filter(a, range(1, 11))))


# ============================================================
# TOPIC: filter() — Armstrong Numbers
# ============================================================

def p(n):
    sum = 0
    dup = n
    p = len(str(n))
    while n > 0:
        rem = n % 10
        sum += rem ** p
        n //= 10
    return True if sum == dup else False

d = filter(p, range(1, 101))
for i in d:
    print(i)


# ============================================================
# TOPIC: filter() — Filter Even-Length Strings
# ============================================================

def s(n):
    return len(n) % 2 == 0

print(list(filter(s, ['12345', '234'])))


# ============================================================
# TOPIC: map() + filter() — Combined Use
# ============================================================

# Sum of even digits in each number
def a(n):
    sum = 0
    while n > 0:
        rem = n % 10
        if rem % 2 == 0:
            sum += rem
        n //= 10
    return sum

print(list(map(a, list(map(int, input().split())))))


# map() — Armstrong check (returns True/False per number)
def p(n):
    sum = 0
    dup = n
    p = len(str(n))
    while n > 0:
        rem = n % 10
        sum += rem ** p
        n //= 10
    return True if sum == dup else False

print(list(map(p, range(1, 101))))
