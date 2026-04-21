# ============================================================
# TOPIC: Complex Numbers
# ============================================================

a = 4 + 5j
print(a)          # (4+5j)
print(type(a))    # <class 'complex'>
print(a.real)     # 4.0
print(a.imag)     # 5.0


# ============================================================
# TOPIC: Strings — Basics & Slicing
# ============================================================

s = "hello"
print(s)

# Slicing
s = "hello world"
print(s[1:4:1])    # 'ell'

# slice() object
s = "slice is not a money app"
i = slice(4, 8, 1)
print(s[i])        # 'e is'


# ============================================================
# TOPIC: String Methods
# ============================================================

s = "Hell20 Wor5ld"
print(s.upper())       # HELL20 WOR5LD
print(s.lower())       # hell20 wor5ld
print(s.swapcase())    # hELL20 wOR5LD
print(s.split())       # ['Hell20', 'Wor5ld']
print(s.split('l'))    # ['He', '', '20 Wor5', 'd']

s = 'we thought to study everyday'
print(s.split('t', 2))    # ['we ', 'hough', ' to study everyday']
print(s.count('t'))        # 4
print(s.replace('t', 'a'))
print(s.replace('t', 'a', 2))
print(s.index('t'))        # 3
print(s.index('t', 4, 10))

s = 'superstar sundar'
print(s.rindex('s'))       # 10
print(s.find('r'))         # 4
print(s.rfind('r', 5))     # 15
print(s.title())           # 'Superstar Sundar'
print(s.isupper())         # False
print(s.islower())         # True
print(s.isalpha())         # False
print(s.isdigit())         # False
print(s.startswith('s'))   # True
print(s.endswith('s'))     # False
print(s.strip('s'))        # 'uperstar sundar'
print(s.lstrip('s'))       # 'uperstar sundar'
print(s.rstrip('r'))       # 'superstar sunda'


# ============================================================
# TOPIC: List Methods
# ============================================================

l = [1, 2, 3, 4, 5]
l.append('a')
print(l)         # [1, 2, 3, 4, 5, 'a']

l.insert(3, 'b')
print(l)         # [1, 2, 3, 'b', 4, 5, 'a']

l.extend('l')
print(l)

l.remove(3)
print(l)

l.pop()
l.pop(3)
print(l)

l.clear()

l = ['a', 'O', 'y', 'A']
l.sort()
print(l)         # ['A', 'O', 'a', 'y']

l.sort(reverse=True)
print(l)         # ['y', 'a', 'O', 'A']

print('@'.join(l))
print(l.index('a'))

l.reverse()
print(l)

dup = l.copy()
print(id(dup) == id(l))    # False — different objects


# ============================================================
# TOPIC: Tuple Methods
# ============================================================

t = (1, 2, 3, 4, 5, 5, 6, 7, 8)
print(t.count(5))    # 2
print(t.index(5))    # 4


# ============================================================
# TOPIC: Set Methods
# ============================================================

s = {4, 'a', 3, 4, 5}
print(s)        # {3, 4, 5, 'a'}

s.add(6)
print(s)

s1 = {1, 2, 3}
s2 = {4, 5, 6}
print(s1.union(s2))           # {1, 2, 3, 4, 5, 6}

s2.add(3)
print(s1.intersection(s2))    # {3}
print(s1.difference(s2))      # {1, 2}


# ============================================================
# TOPIC: Dictionary Methods
# ============================================================

d = {'a': 1, 'c': 4}
d['c'] = 400
print(d)

d.pop('b') if 'b' in d else None
d.popitem()

d = {'c': 'b', 'b': 'g'}
print(d.get('b'))           # 'g'
print(d.get('a'))           # None
print(d.setdefault('b', 56))
print(d.setdefault('x'))    # None

print(d.keys())
print(d.values())
print(d.items())

d = {}
print(d.fromkeys('abcd', 5678))     # {'a': 5678, 'b': 5678, ...}
l = [2, 3, 4]
print(d.fromkeys(l))                # {2: None, 3: None, 4: None}
