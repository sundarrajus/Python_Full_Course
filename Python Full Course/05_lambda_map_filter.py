# ============================================================
# TOPIC: Lambda — Basics
# ============================================================

var = lambda a, b, c: a + b + c
print(var(2, 3, 4))

print((lambda a: a * a)(2))

for i in range(5, 11):
    print((lambda a: a ** 3)(i), end=' ')
print()


# ============================================================
# TOPIC: map() — With Named Functions
# ============================================================

def sample(num):
    ans = num * num
    return ans

mapobj = map(sample, range(2, 8))
for ans in mapobj:
    print(ans)


def f(n):
    return 'even' if n % 2 == 0 else 'odd'

print(list(map(f, range(1, 51))))


# Armstrong numbers using map
def arm(n):
    sum = 0
    dup = n
    p = len(str(n))
    while n > 0:
        rem = n % 10
        sum = sum + rem ** p
        n //= 10
    return 'arm' if sum == dup else 'not'

print(list(map(arm, range(1, 501))))


# Sum of digits using map
def s(n):
    sum = 0
    while n > 0:
        rem = n % 10
        sum = sum + rem
        n //= 10
    return sum

print(list(map(s, [34567, 598765, 70, 8, 9])))


# map() with two lists
def s(n, m):
    return n * m

print(list(map(s, [2, 4, 6, 8], [1, 3, 5, 7, 9])))


# ============================================================
# TOPIC: map() — With Lambda
# ============================================================

print(list(map(lambda a: a ** 2, range(2, 8))))
print(list(map(lambda n, m: n + m, [1, 2, 3, 4, 5], [6, 7, 8, 9, 0])))


# ============================================================
# TOPIC: map() — Patterns with Lambda
# ============================================================

# Right-angle triangle pattern
num = 5
print('\n'.join(list(map(lambda i: '* ' * i, range(1, num + 1)))))


# Inverted triangle pattern
num = 5
print('\n'.join(list(map(lambda i: '* ' * i, range(num, 0, -1)))))


# Right-aligned pattern
num = 5
print('\n'.join(list(map(lambda sp, st: '  ' * sp + '* ' * st, range(0, num), range(num, 0, -1)))))
