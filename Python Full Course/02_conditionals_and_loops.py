# ============================================================
# TOPIC: if-elif-else — Conditionals
# ============================================================

s = input("enter the string: ").title()
if s == 'Bengaluru':
    print("register")


a, b, c, d = map(int, input().split())
if a > b and a > c and a > d:
    print('a is greater')
elif b > c and b > d:
    print('b is greater')
elif c > d:
    print('c is greater')
else:
    print('d is greater')


n = 25
if n % 2 == 0:
    print('2 is the factor')
elif n % 5 == 0:
    print('5 is the factor')
elif n % 7 == 0:
    print('7 is the factor')
elif n % 3 == 0:
    print('3 is the factor')
else:
    print('no factor')


n = 0
print('even' if n % 2 == 0 else 'not')


# ============================================================
# TOPIC: for Loop — Iterating Strings, Lists, Dicts
# ============================================================

s = 'sundar'
for char in s:
    print(char)


l = [6, 3.5, 'asdf', [2, 5, 'xcv'], 24, 'sdfgh']
for ele in l:
    print(ele)


d = {1: 2, 3: 'asdfg', 'd': 90}
for key, value in d.items():
    print(key, value, sep=':')


for i in range(0, 21, 2):
    print(i)


# ============================================================
# TOPIC: for Loop — Number Programs
# ============================================================

# Prime number check
a = int(input())
count = 0
for i in range(1, a + 1):
    if a % i == 0:
        count += 1
if count == 2:
    print("Prime number")
else:
    print("Not a prime number")


# Factorial using for
num = 5
fact = 1
if num > 0:
    for i in range(1, num + 1):
        fact *= i
    print(f'fact of {num} is {fact}')
else:
    print('not possible')


# Perfect number
num = int(input())
count = 0
for i in range(1, num):
    if num % i == 0:
        count += i
if count == num:
    print("perfect number")
else:
    print("not perfect")


# Print all primes up to n
a = 10
for n in range(2, a + 1):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        print(n)


# ============================================================
# TOPIC: while Loop — Number Programs
# ============================================================

# Factorial using while
n = int(input())
fact = 1
val = 1
if n > 0:
    while val <= n:
        fact *= val
        val += 1
    print(f'factorial of {n} is {fact}')
else:
    print(f'factorial of {n} is not possible')


# Count digits
n = 123456789
count = 0
while n != 0:
    n //= 10
    count += 1
print(count)


# Sum of digits
n = int(input())
sum = 0
while n > 0:
    rem = n % 10
    sum += rem
    n //= 10
print(sum)


# Spy number
n = int(input())
sum = 0
mul = 1
while n > 0:
    rem = n % 10
    sum += rem
    mul *= rem
    n //= 10
if sum == mul:
    print("spy number")
else:
    print("not a spy number")


# Armstrong number
n = 370
dup = n
sum = 0
power = len(str(n))
while n > 0:
    rem = n % 10
    sum += rem ** power
    n //= 10
if sum == dup:
    print("armstrong number")
else:
    print("not an armstrong number")


# Disarium number
n = int(input())
sum = 0
dup = n
power = len(str(n))
while n > 0:
    rem = n % 10
    sum += rem ** power
    n //= 10
    power -= 1
if sum == dup:
    print("disarum")
else:
    print("not")


# Reverse a number
n = int(input())
sum = 0
while n > 0:
    rem = n % 10
    sum = sum * 10 + rem
    n //= 10
print(sum)


# LCM using while
n1, n2 = 10, 15
lcm = max(n1, n2)
while True:
    if lcm % n1 == 0 and lcm % n2 == 0:
        print(lcm)
        break
    else:
        lcm += 1


# Integer to Binary
n = 8
p = 1
sum = 0
while n > 0:
    rem = n % 2
    sum = sum + rem * p
    n //= 2
    p *= 10
print(sum)


# Binary to Integer
n = 1000
sum = 0
p = 0
while n > 0:
    rem = n % 10
    sum = sum + rem * (2 ** p)
    n //= 10
    p += 1
print(sum)


# Strong number
n = int(input())
dup = n
sum = 0
while n > 0:
    rem = n % 10
    fact = 1
    for i in range(1, rem + 1):
        fact = fact * i
    sum = sum + fact
    n //= 10
print("strong number" if dup == sum else "not")


# Palindrome prime (Pali-prime)
n = int(input())
count = 0
for i in range(1, n // 2 + 1):
    if n % i == 0:
        count += 1
if count == 2:
    sum = 0
    dup = n
    while n > 0:
        rem = n % 10
        sum = sum * 10 + rem
        n //= 10
    print("paliprime number" if dup == sum else "not")
else:
    print("not")


# EMIRP number
n = int(input())
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count += 1
if count == 2:
    sum = 0
    dup = n
    while n > 0:
        rem = n % 10
        sum = sum * 10 + rem
        n //= 10
    if sum != dup:
        count2 = 0
        for i in range(1, sum + 1):
            if sum % i == 0:
                count2 += 1
        if count2 == 2:
            print("EMIRP number")
        else:
            print("not")
    else:
        print("not")
else:
    print("not")


# Happy number
n = 13
while n > 9:
    sum = 0
    while n > 0:
        rem = n % 10
        sum = sum + rem ** 2
        n //= 10
    n = sum
print('happy number' if sum == 1 or sum == 7 else 'not')


# ============================================================
# TOPIC: for-else and while-else
# ============================================================

for i in range(2, 7):
    print(i)
else:
    print("hello")


num = 1
while num != 8:
    print(num)
    num += 1
else:
    print('hello')


# ============================================================
# TOPIC: Nested Loops
# ============================================================

for i in range(7, 5, -1):
    print("os")
    for j in range(-1, -3, -1):
        print("is")
    print("oe")


for i in range(7, 5, -1):
    for j in range(2, 6):
        for k in range(6, 9):
            print(i, j, k)


# ============================================================
# TOPIC: break and continue
# ============================================================

for i in range(3, 9):
    if i % 2 == 0:
        print("even")
        break
    print("hello")


for val in range(0, 10):
    if val % 2 == 0:
        print("even")
    continue
    print("odd")    # never reached
