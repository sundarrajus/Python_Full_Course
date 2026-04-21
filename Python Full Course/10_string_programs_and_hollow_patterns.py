# ============================================================
# TOPIC: String Programs — Reverse a String
# ============================================================

s = 'abcdefg'
a = ''
for ch in s:
    a = ch + a
print(a)


# ============================================================
# TOPIC: String Programs — Palindrome Check
# ============================================================

s = 'madam'
for i in range(0, len(s) // 2):
    if s[i] != s[-i - 1]:
        print('not palindrome')
        break
else:
    print('palindrome')


# ============================================================
# TOPIC: String Programs — Remove Duplicate Characters
# ============================================================

s = 'engineering'
a = ''
for ch in s:
    if ch not in a:
        a += ch
print(a)


# ============================================================
# TOPIC: String Programs — Case Conversion (Manual)
# ============================================================

s = 'We wiLl uget p* or p1'
res = ''
for ch in s:
    if 'a' <= ch <= 'z':
        res += chr(ord(ch) - 32)    # lower to upper
    elif 'A' <= ch <= 'Z':
        res += chr(ord(ch) + 32)    # upper to lower
    else:
        res += ch
print(res)


# ============================================================
# TOPIC: String Programs — Count Digits and Special Characters
# ============================================================

s = 'a7bf5j3'
c = 0
for ch in s:
    if '0' <= ch <= '9':
        c += 1
print(c)    # count of digits


s = 'We wiLl &uget p* @or p1'
c = 0
for ch in s:
    if '0' <= ch <= '9' or 'A' <= ch <= 'Z' or 'a' <= ch <= 'z':
        pass
    else:
        c += 1
print(c)    # count of special characters


# ============================================================
# TOPIC: String Programs — All Substrings
# ============================================================

s = 'abcde'
for si in range(0, len(s)):
    for ev in range(si + 1, len(s) + 1):
        print(s[si:ev])


# ============================================================
# TOPIC: String Programs — Palindrome Substrings
# ============================================================

s = 'level'
for si in range(0, len(s)):
    for ev in range(si + 1, len(s) + 1):
        a = s[si:ev]
        if a == a[::-1]:
            print(a)


# ============================================================
# TOPIC: String Programs — Vowels and Consonants
# ============================================================

s = 'asdftyuiopokjhbvc'
r = ''
for ch in s:
    if ch in 'aeiouAEIOU':
        r += ch
print(r)    # vowels

r = ''
for ch in s:
    if ch not in 'aeiouAEIOU':
        r += ch
print(r)    # consonants


# ============================================================
# TOPIC: String Programs — Run-Length Encoding
# ============================================================

s = 'aaaabbcccdd'
r = ''
c = 1
for i in range(0, len(s) - 1):
    if s[i] == s[i + 1]:
        c += 1
    else:
        r += str(c) + s[i]
        c = 1
r += str(c) + s[i + 1]
print(r)


# ============================================================
# TOPIC: String Programs — Frequency Count
# ============================================================

s = 'engineering'
a = ''
for ch in s:
    if ch not in a:
        a += ch
for ele in a:
    print(f'{ele}:{s.count(ele)}')


# ============================================================
# TOPIC: String Programs — Anagram Check
# ============================================================

s1 = 'listen'
s2 = 'silent'
if len(s1) != len(s2):
    print('not anagram')
else:
    if sorted(s1) == sorted(s2):
        print('anagram')
    else:
        print('not')


# ============================================================
# TOPIC: String Programs — Reverse Words
# ============================================================

s = 'hello world hi'
r = ''
a = s.split()
for ch in a:
    r = ch + ' ' + r
print(r)


# ============================================================
# TOPIC: String Programs — Pangram Check
# ============================================================

s = 'the quick brown fox jumps over the lazy dog'
s = s.lower()
letters = set()
for ch in s:
    if ch.isalpha():
        letters.add(ch)
if len(letters) == 26:
    print('panagram')
else:
    print('not')


# ============================================================
# TOPIC: Hollow Patterns — Rectangle
# ============================================================

num = 5
star = num
space = 0
for row in range(1, num + 1):
    for sp in range(1, space + 1):
        print(' ', end=' ')
    for col in range(1, star + 1):
        if row == 1 or row == num or col == star or col == 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
    if row <= num // 2:
        star -= 2
        space += 1
    else:
        space -= 1
        star += 2
