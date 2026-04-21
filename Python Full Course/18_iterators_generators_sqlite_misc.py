# ============================================================
# TOPIC: Iterators — iter() and next()
# ============================================================

# Tuple iterator
# a = ('a', 6, 3)
# it = iter(a)
# while True:
#     print(next(it))   # raises StopIteration when exhausted


# Custom iterator — odd numbers in range
# class OddRange:
#     def __init__(self, i, j):
#         self.i = i
#         self.j = j
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.i > self.j:
#             raise StopIteration
#         var = self.i
#         self.i += 2
#         return var
# obj = OddRange(1, 11)
# for val in obj:
#     print(val)


# Custom iterator — alphabet range
# class AlphaRange:
#     def __init__(self, i, j):
#         self.i = i
#         self.j = j
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if ord(self.i) > ord(self.j):
#             raise StopIteration
#         var = self.i
#         self.i = chr(ord(self.i) + 1)
#         return var
# obj = AlphaRange('a', 'z')
# for ch in obj:
#     print(ch)


# ============================================================
# TOPIC: Generators — yield keyword
# ============================================================

# Simple generator
# def gen():
#     yield 'a'
#     yield 2
#     yield 3
# g = gen()
# print(next(g))
# print(next(g))
# print(next(g))


# Factorial generator
# def factorial_gen(n):
#     if n <= 0:
#         yield 1
#     fact = 1
#     for i in range(1, n + 1):
#         fact *= i
#         yield fact
# ob = factorial_gen(5)
# for val in ob:
#     print(val)


# Fibonacci generator
# def fibonacci(n):
#     f, s = 0, 1
#     for i in range(n):
#         yield f
#         f, s = s, f + s
# for val in fibonacci(6):
#     print(val)


# ============================================================
# TOPIC: SQLite3 — Create Table and Insert
# ============================================================

# import sqlite3
# conn = sqlite3.connect("mock.db")
# cur = conn.cursor()
# cur.execute('''
#     CREATE TABLE mockdetails (
#         sno NUMBER PRIMARY KEY,
#         name VARCHAR NOT NULL,
#         mobno NUMBER UNIQUE,
#         result VARCHAR DEFAULT "absent"
#     )
# ''')
# conn.commit()
# cur.execute("INSERT INTO mockdetails VALUES (1, 'sundar', 234567, 'p1')")
# conn.commit()


# ============================================================
# TOPIC: Matrix Operations
# ============================================================

# Matrix addition
# m1 = [[1,2,3],[4,5,6],[7,8,9]]
# m2 = [[9,8,7],[6,5,4],[3,2,1]]
# if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
#     for row in range(len(m1)):
#         for col in range(len(m1[0])):
#             m2[row][col] += m1[row][col]
#     print(m2)
# else:
#     print('not possible')

# Matrix multiplication
# m1 = [[1,2,3],[4,5,6],[7,8,9]]
# m2 = [[9,8,7],[6,5,4],[3,2,1]]
# mat = []
# for row in range(len(m1)):
#     line = []
#     for col in range(len(m2[0])):
#         ele = 0
#         for op in range(len(m2)):
#             ele += m1[row][op] * m2[op][col]
#         line.append(ele)
#     mat.append(line)
# print(mat)

# Transpose
# m1 = [[1,2,3],[4,5,6],[7,8,9]]
# mat = []
# for row in range(len(m1)):
#     line = []
#     for col in range(len(m1[0]) - 1, -1, -1):
#         line.append(m1[col][row])
#     mat.append(line)
# print(mat)


# ============================================================
# TOPIC: Misc — Find Duplicate Elements in a List
# ============================================================

l = [1, 4, 0, 4, 6, 0, 7]
seen = []
for i in l:
    if i in seen:
        print(i)
    else:
        seen.append(i)
