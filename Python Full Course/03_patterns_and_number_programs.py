# ============================================================
# TOPIC: Star Patterns — Square
# ============================================================

for i in range(1, 5):
    for j in range(1, 5):
        print('*', end=' ')
    print()


# ============================================================
# TOPIC: Star Patterns — Right Triangle (increasing)
# ============================================================

num = 4
stars = 1
spaces = num - 1
for i in range(1, num + 1):
    for sp in range(1, spaces + 1):
        print(' ', end=' ')
    for st in range(1, stars + 1):
        print('*', end=' ')
    print()
    stars += 2
    spaces -= 1


# ============================================================
# TOPIC: Star Patterns — Inverted Triangle
# ============================================================

num = 4
stars = 2 * num - 1
spaces = 0
for i in range(1, num + 1):
    for sp in range(1, spaces + 1):
        print(' ', end=' ')
    for st in range(1, stars + 1):
        print('*', end=' ')
    print()
    stars -= 2
    spaces += 1


# ============================================================
# TOPIC: Star Patterns — Diamond (odd num)
# ============================================================

num = 5
stars = num
spaces = 0
for i in range(1, num + 1):
    for sp in range(1, spaces + 1):
        print(' ', end=' ')
    for st in range(1, stars + 1):
        print('*', end=' ')
    print()
    if i < num // 2 + 1:
        stars -= 2
        spaces += 1
    else:
        stars += 2
        spaces -= 1


# ============================================================
# TOPIC: Number Patterns — Repeating Row Value
# ============================================================

num = 5
for i in range(num, 0, -1):
    for n in range(1, i + 1):
        print(i, end=' ')
    print()


# ============================================================
# TOPIC: Number Patterns — Increasing Sequence Per Row
# ============================================================

num = 5
for ev in range(num, 0, -1):
    for i in range(1, ev + 1):
        print(i, end=' ')
    print()


num = 5
for sv in range(num, 0, -1):
    for i in range(sv, num + 1):
        print(i, end=' ')
    print()


num = 5
for sv in range(1, num + 1):
    for i in range(sv, num + 1):
        print(i, end=' ')
    print()


num = 5
for sv in range(1, num + 1):
    for i in range(sv, 0, -1):
        print(i, end=' ')
    print()


num = 5
for sv in range(num, 0, -1):
    for i in range(sv, 0, -1):
        print(i, end=' ')
    print()


num = 5
for ev in range(0, num):
    for i in range(num, ev, -1):
        print(i, end=' ')
    print()


# ============================================================
# TOPIC: Number Patterns — With Spaces
# ============================================================

num = 5
spaces = 0
for ev in range(num, 0, -1):
    for sp in range(1, spaces + 1):
        print(' ', end=' ')
    for i in range(1, ev + 1):
        print(i, end=' ')
    print()
    spaces += 1


num = 5
spaces = num - 1
for ev in range(num - 1, -1, -1):
    for sp in range(1, spaces + 1):
        print(' ', end=' ')
    for i in range(num, ev, -1):
        print(i, end=' ')
    print()
    spaces -= 1


num = 5
for row in range(num):
    for sp in range(row):
        print("  ", end="")
    for i in range(num, row, -1):
        print(i, end=" ")
    print()


num = 4
spaces = 0
for ev in range(num * 2, 1, -2):
    for sp in range(1, spaces + 1):
        print("  ", end="")
    for val in range(1, ev):
        print(val, end=' ')
    print()
    spaces += 1
