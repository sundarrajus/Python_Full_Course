# ============================================================
# TOPIC: File Handling — Read Modes
# ============================================================

# read() — basic file reading
# fobj = open('hello.txt', encoding='utf-8')
# print(fobj.readable())
# print(fobj.read(4))
# print(fobj.read())
# print(fobj.readline(4))
# print(fobj.readline())
# print(fobj.tell())
# print(fobj.readlines())


# ============================================================
# TOPIC: File Handling — Write Mode
# ============================================================

# write() — opens new file and deletes old data
# fobj = open('hi_hello.txt', 'w')
# print(fobj.writable())
# print(fobj.tell())
# fobj.write('hi hello')
# fobj.write('string')
# fobj.writelines('hi\n hello\n')
# fobj.close()


# ============================================================
# TOPIC: File Handling — Append, Exclusive, r+, w+, a+ Modes
# ============================================================

# append mode
# fobj = open('hi_hello1.txt', 'a')
# print(fobj.writable())

# exclusive mode
# fobj = open('hi_hello3.txt', 'x')
# print(fobj)

# r+ mode
# fobj = open('hi_hello.txt', 'r+')
# print(fobj.readable())
# print(fobj.writable())
# fobj.write('23456789')
# print(fobj.read())
# fobj.close()

# w+ mode
# fobj = open('hi_hello1.txt', 'w+')
# print(fobj.writable())
# print(fobj.readable())
# print(fobj.tell())
# fobj.write('asdfghjkiuytrewqasdfghjk')
# print(fobj.tell())
# fobj.seek(0)
# print(fobj.read())

# a+ mode
# fobj = open('hi_hello1.txt', 'a+')
# print(fobj.writable())
# print(fobj.readable())
# print(fobj.tell())
# fobj.write('hello')
# print(fobj.read())
# fobj.close()


# ============================================================
# TOPIC: File Handling — Practical Programs with 'with' Block
# ============================================================

# Write prime numbers to file, then count lines and digits
# with open('hi_hello.txt', 'w') as fobj:
#     def prime(n):
#         if n > 1:
#             for i in range(2, int(n * 0.5) + 1):
#                 if n % i == 0:
#                     return False
#             return True
#         return False
#     for ele in filter(prime, range(1, 101)):
#         fobj.write(str(ele) + '\n')
#
# with open('hi_hello.txt', 'r') as fobj:
#     print(len(fobj.readlines()))
#
# with open('hi_hello1.txt', 'r') as fobj:
#     c = 0
#     for i in fobj:
#         i = i.strip('\n')
#         c += len(i)
#     print(c)
#
# with open('hi_hello.txt', 'r') as fobj:
#     c = 0
#     for i in fobj:
#         i = i.strip('\n')
#         for l in i:
#             if '0' <= l <= '9':
#                 c += 1
#     print(c)
#
# import os
# os.rename('hi_hello.txt', 'hii.txt')


# ============================================================
# TOPIC: JSON — dumps() and dump()
# ============================================================

# import json
# print(json.dumps(None))
# print(json.dumps(True))
# print(json.dumps(23))
# print(json.dumps('abc'))
#
# d = {'a': 12345, 'b': 567}
# with open('content.json', 'w') as fobj:
#     json.dump(d, fobj, indent=4)


# ============================================================
# TOPIC: Regular Expressions — Basic Functions
# ============================================================

# import re
# s = 'we want mock interview tommorrow'
# print(re.match('w', s))
# print(re.match('a', s))
# print(re.search('w', s))
# print(re.findall('w', s))
# print(re.split('e', s))
# print(re.split('e', s, 2))
# print(re.sub('e', 'a', s, 2))
# print(re.subn('e', 'w', s))
# print(re.finditer('e', s))


# ============================================================
# TOPIC: Regular Expressions — Meta Characters
# ============================================================

# import re
# s = 'a@b@5.#h$s%\t^.a&d*h'
# print(re.findall('.', s))
# print(re.findall('[.]', s))
# print(re.findall('\.', s))
# print(re.findall('^a', s))
# print(re.findall('h$', s))
#
# s = 'ab abc accb abba abbba acccb'
# print(re.findall('ab*c', s))
# print(re.findall('ab*c*', s))
# print(re.findall('ab+c', s))
# print(re.findall('ab?c', s))


# ============================================================
# TOPIC: Regular Expressions — Special Sequences and Sets
# ============================================================

# import re
# s = 'a@_cb 3c (A6_Bab'
# print(re.findall('^a', s))
# print(re.findall('a\Z', s))
#
# s = 'aA6b5bcyT'
# print(re.findall(r'T\b', s))
# print(re.findall(r'\ba', s))
#
# s = 'anyti$me an(ywher^e7 or 53 sin$gle hand'
# print(re.findall('[arn]', s))
# print(re.findall('[abcde]', s))
# print(re.findall('[^arn]', s))
# print(re.findall('[0-9]', s))
# print(re.findall('[$]', s))


# ============================================================
# TOPIC: Regular Expressions — Phone Number & Email Validation
# ============================================================

import re

s = '+91-8978723679'
if re.match(r'^[+]91( |-)?[6789][0-9]{9}$', s):
    print('valid')
else:
    print('not valid')


import re

s = 'shavalasundarraju@gmail.com'
if re.match(r'^[a-z]+@gmail[.]com', s):
    print('valid')
else:
    print('not valid')
