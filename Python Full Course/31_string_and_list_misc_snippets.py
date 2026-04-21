# ============================================================
# TOPIC: Recursion — Integer to Binary
# ============================================================

# def int_to_binary(n, p=1):
#     if n == 0:
#         return 0
#     return (n % 2) * p + int_to_binary(n // 2, p * 10)
# print(int_to_binary(8))


# ============================================================
# TOPIC: Recursion — Count Factors (Prime Check Helper)
# ============================================================

# def count_factors(n, val):
#     if val == n + 1:
#         return 0
#     if n % val == 0:
#         return 1 + count_factors(n, val + 1)
#     else:
#         return 0 + count_factors(n, val + 1)
# print(count_factors(15, 1))


# ============================================================
# TOPIC: Recursion — Reverse a Number
# ============================================================

# def reverse_num(n, place):
#     if n == 0:
#         return 0
#     return (n % 10) * place + reverse_num(n // 10, place // 10)
# n = 123
# place = 10 ** (len(str(n)) - 1)
# print(reverse_num(n, place))


# ============================================================
# TOPIC: String — Remove Duplicate Characters
# ============================================================

# s = 'engineering'
# a = ''
# for ch in s:
#     if ch not in a:
#         a += ch
# print(a)


# ============================================================
# TOPIC: String — Run-Length Encoding
# ============================================================

# s = 'aaabbccdddd'
# res = ''
# count = 1
# for i in range(len(s) - 1):
#     if s[i] == s[i + 1]:
#         count += 1
#     else:
#         res += str(count) + s[i]
#         count = 1
# res += str(count) + s[-1]
# print(res)


# ============================================================
# TOPIC: List — Reverse a List
# ============================================================

l = [1, 2, 3, 4]
print(l[::-1])
