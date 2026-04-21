# ============================================================
# TOPIC: Copy Operations — Normal, Shallow, Deep Copy
# ============================================================

# Normal copy (same reference)
# l = [1, 2, 3, 4]
# dup = l
# print(id(l))
# print(id(dup))   # same id — both point to same object

# Shallow copy — slicing
# l = [1, 2, 3, 4]
# dup = l[::]
# print(l is dup)   # False
# l[0] = 10
# print(l)
# print(dup)

# Shallow copy — .copy()
# l = [12, 3, 4]
# dup = l.copy()
# print(l is dup)   # False
# dup[0] = 10
# print(l)
# print(dup)

# Deep copy — copy.deepcopy()
# import copy
# l = [12, 3, 4]
# dup = copy.deepcopy(l)
# print(l is dup)
# l[0] = 10
# print(l[0] is dup[0])
# print(l)
# print(dup)


# ============================================================
# TOPIC: Exception Handling — try / except / else / finally
# ============================================================

try:
    l = [1, 2, 3, 4]
    s = 0
    for i in l:
        s += i
    print(s)
except Exception as msg:
    print(msg)
else:
    print('hi')
finally:
    print('program done')
