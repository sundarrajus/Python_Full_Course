# ============================================================
# TOPIC: List Programs — Frequency Count (Active Code)
# ============================================================

s = 'engineering'
a = ''
for ch in s:
    if ch not in a:
        a += ch
for e in a:
    print(f'{e}: {s.count(e)}')
print(a)


# ============================================================
# TOPIC: List Programs — Reverse a List
# ============================================================

l = [1, 2, 3, 4, 5]
a = []
for i in l:
    a = [i] + a
print(a)


# ============================================================
# TOPIC: List Programs — Find Pair with Given Sum
# ============================================================

l = [6, 3, 5, 2, 7, 1, 4, 0]
t = 7
for i in range(0, len(l) - 1):
    for j in range(i + 1, len(l)):
        if l[i] + l[j] == t:
            print(l[i], l[j])


# ============================================================
# TOPIC: List Comprehension — Basics
# ============================================================

print([i for i in range(1, 10)])
print([i * i for i in range(1, 10)])
print(['hello' for i in range(1, 10)])

l = 'abcdefghijklmnopqrstuvwxyz'
print([l[i] for i in range(0, len(l))])

s = 'abcd'
print([s[i] * (i + 1) for i in range(0, len(s))])

print([i for i in range(0, 11) if i % 2 == 0])

val = 7
if len([i for i in range(1, val + 1) if val % i == 0]) == 2:
    print('prime')
else:
    print('not prime')

print(['even' if i % 2 == 0 else 'odd' for i in range(1, 11)])

print([[i, j] for i in range(1, 4) for j in range(3, 6)])

a, b, c, t = 3, 6, 4, 5
print([[i, j, k] for i in range(a) for j in range(b) for k in range(c) if i + j + k == t])


# ============================================================
# TOPIC: Matrix — Addition
# ============================================================

m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
    for row in range(len(m1)):
        for col in range(len(m1[0])):
            m1[row][col] += m2[row][col]
    print(m1)
else:
    print('not')


# ============================================================
# TOPIC: Matrix — Multiplication
# ============================================================

m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
a = []
for i in range(len(m1)):
    line = []
    for j in range(len(m2[0])):
        res = 0
        for k in range(len(m2)):
            res += m1[i][k] * m2[k][j]
        line.append(res)
    a.append(line)
print(a)


# ============================================================
# TOPIC: Matrix — Rotate 90 Degrees
# ============================================================

m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
a = []
for i in range(len(m1)):
    line = []
    for j in range(len(m1[0]) - 1, -1, -1):
        line.append(m1[j][i])
    a.append(line)
print(a)


# ============================================================
# TOPIC: Matrix — Rotate 180 Degrees
# ============================================================

m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
a = []
for i in range(len(m1) - 1, -1, -1):
    line = []
    for j in range(len(m1[0]) - 1, -1, -1):
        line.append(m1[i][j])
    a.append(line)
print(a)


# ============================================================
# TOPIC: Matrix — Rotate 270 Degrees
# ============================================================

m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
a = []
for i in range(len(m1) - 1, -1, -1):
    line = []
    for j in range(len(m1[0])):
        line.append(m1[j][i])
    a.append(line)
print(a)
