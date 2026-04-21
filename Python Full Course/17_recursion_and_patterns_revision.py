# ============================================================
# TOPIC: Number Programs — Digit Sum, Spy, Armstrong (Revision)
# ============================================================

# Digit sum
# n = 1234
# s = 0
# while n > 0:
#     rem = n % 10
#     s += rem
#     n //= 10
# print(s)

# Spy number (sum of digits == product of digits)
# n = 123
# s, mul = 0, 1
# while n > 0:
#     rem = n % 10
#     s += rem
#     mul *= rem
#     n //= 10
# print('spy' if s == mul else 'not')

# Armstrong number
# n = 153
# dup = n
# p = len(str(n))
# s = 0
# while n > 0:
#     rem = n % 10
#     s += rem ** p
#     n //= 10
# print('arm' if s == dup else 'not')


# ============================================================
# TOPIC: Pattern Programs (Revision)
# ============================================================

# Right-angle star triangle (decreasing)
# num = 5
# for i in range(num, 0, -1):
#     for j in range(1, i + 1):
#         print('*', end=' ')
#     print()

# Pyramid (right-aligned)
# num = 5
# star = 1
# space = num - 1
# for row in range(1, num + 1):
#     for s in range(1, space + 1):
#         print(' ', end=' ')
#     for s in range(1, star + 1):
#         print('*', end=' ')
#     print()
#     star += 1
#     space -= 1

# Diamond pattern
# num = 5
# star = 1
# space = num // 2
# for row in range(1, num + 1):
#     for s in range(1, space + 1):
#         print(' ', end=' ')
#     for s in range(1, star + 1):
#         print('*', end=' ')
#     print()
#     if row < (num // 2) + 1:
#         star += 2
#         space -= 1
#     else:
#         star -= 2
#         space += 1

# Number patterns (various)
# num = 5
# for i in range(1, num + 1):
#     for j in range(1, i + 1):
#         print(i, end=' ')
#     print()

# num = 5
# for ev in range(num + 1, 0, -1):
#     for val in range(1, ev):
#         print(val, end=' ')
#     print()


# ============================================================
# TOPIC: Recursion — Emirp Number Check
# ============================================================

def count_factors(n, v=1):
    if v == n + 1:
        return 0
    if n % v == 0:
        return 1 + count_factors(n, v + 1)
    else:
        return 0 + count_factors(n, v + 1)


def reverse_num(n, p):
    if n == 0:
        return 0
    return (n % 10) * p + reverse_num(n // 10, p // 10)


def emirp(n):
    power = 10 ** (len(str(n)) - 1)
    rev = reverse_num(n, power)
    if count_factors(n) == 2 and rev != n and count_factors(rev) == 2:
        return 'EMIRP'
    return 'not'


n = 13
print(emirp(n))
