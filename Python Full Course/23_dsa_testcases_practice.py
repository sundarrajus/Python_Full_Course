# ============================================================
# TOPIC: DSA Test Cases Practice — All Programs (Commented)
# ============================================================

# Each block below is a standalone program.
# Uncomment the block you want to run.

# Even or Odd
# n = int(input("enter your value : "))
# print("even" if n % 2 == 0 else "odd")


# Prime or Not
# count = 0
# for i in range(1, n):
#     if n % i == 0:
#         count += 1
# print("prime" if count == 2 else "not prime")


# Factorial
# fact = 1
# for i in range(1, n + 1):
#     fact *= i
# print(f'Factorial of {n} is :', fact)


# Fibonacci Series
# a, b = 0, 1
# print(a)
# print(b)
# for i in range(n):
#     c = a + b
#     print(c)
#     a, b = b, c


# Reverse of a Number
# s = 0
# while n > 0:
#     rem = n % 10
#     s = s * 10 + rem
#     n //= 10
# print(s)


# Palindrome Number
# dup = n
# s = 0
# while n > 0:
#     rem = n % 10
#     s = s * 10 + rem
#     n //= 10
# print("Palindrome" if s == dup else "not palindrome")


# Armstrong Number
# p = len(str(n))
# dup = n
# s = 0
# while n > 0:
#     rem = n % 10
#     s += rem ** p
#     n //= 10
# print("armstrong" if s == dup else "not armstrong")


# Sum of Digits
# s = 0
# while n > 0:
#     rem = n % 10
#     s += rem
#     n //= 10
# print(s)


# Maximum of 3 Numbers
# a, b, c = map(int, input().split())
# print(max(a, b, c))


# GCD
# a, b = map(int, input().split())
# while b > 0:
#     a, b = b, a % b
# print("GCD is", a)


# LCM
# import math
# a, b = map(int, input().split())
# lcm = (a * b) // math.gcd(a, b)
# print("lcm is", lcm)


# Co-prime Check
# import math
# a, b = map(int, input().split())
# print("co prime" if math.gcd(a, b) == 1 else "not coprime")


# Leap Year
# if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
#     print("leap year")
# else:
#     print("not a leap year")


# Count Vowels and Consonants
# s = "Sundar Raju"
# v, c = 0, 0
# for i in s:
#     if i.lower() in 'aeiou':
#         v += 1
#     else:
#         c += 1
# print(v, c)


# Reverse a String
# s = "sundar"
# print(s[::-1])


# Anagram Check
# s1, s2 = "listen", "silent"
# print("anagram" if sorted(s1) == sorted(s2) else "not")


# Remove Duplicates from String
# s = "sundarrajus"
# a = ""
# for i in s:
#     if i not in a:
#         a += i
# print(a)


# Second Largest in List
# l = [1, 5, 8, 3, 8, 5]
# a = sorted(set(l))
# print(a[-2])


# Linear Search
# l = [7, 4, 8, 2, 6, 3]
# target = 4
# for i in range(len(l)):
#     if l[i] == target:
#         print(i)
#         break
# else:
#     print(-1)


# Two Sum
# l = [7, 4, 8, 2, 6, 3]
# target = 11
# for i in range(len(l)):
#     for j in range(i + 1, len(l)):
#         if l[i] + l[j] == target:
#             print(i, j)


# Binary Search
# l = [4, 3, 6, 5, 8, 2]
# l.sort()
# target = 8
# low, high = 0, len(l) - 1
# while low <= high:
#     mid = (low + high) // 2
#     if l[mid] > target:
#         high = mid - 1
#     elif l[mid] < target:
#         low = mid + 1
#     else:
#         print(mid)
#         break
# else:
#     print(-1)


# Bubble Sort
# l = [4, 3, 6, 5, 8, 2]
# for i in range(len(l) - 1):
#     for j in range(len(l) - i - 1):
#         if l[j] > l[j + 1]:
#             l[j], l[j + 1] = l[j + 1], l[j]
# print(l)


# Selection Sort
# l = [4, 3, 6, 5, 8, 2]
# for i in range(len(l) - 1):
#     least = i
#     for j in range(i + 1, len(l)):
#         if l[least] > l[j]:
#             least = j
#     l[i], l[least] = l[least], l[i]
# print(l)


# Insertion Sort
# l = [5, 7, 4, 6, 8, 9]
# for i in range(1, len(l)):
#     for j in range(i, 0, -1):
#         if l[j] < l[j - 1]:
#             l[j], l[j - 1] = l[j - 1], l[j]
# print(l)


# Quick Sort
# def f(l):
#     if len(l) <= 1:
#         return l
#     pivot = l[0]
#     left = [ele for ele in l[1:] if ele < pivot]
#     right = [ele for ele in l[1:] if ele >= pivot]
#     return f(left) + [pivot] + f(right)
# l = [3, 6, 4, 2, 8]
# print(f(l))


# Create a Matrix
# rows, columns = 2, 3
# matrix = []
# for r in range(1, rows + 1):
#     line = []
#     for c in range(1, columns + 1):
#         line.append(int(input("enter the element :")))
#     matrix.append(line)
# print(matrix)


# Matrix Addition
# a = [[1,2,3],[4,5,6],[7,8,9]]
# b = [[6,4,8],[7,6,4],[3,6,9]]
# mat = []
# for r in range(len(a)):
#     line = []
#     for c in range(len(a[0])):
#         line.append(a[r][c] + b[r][c])
#     mat.append(line)
# print(mat)


# Matrix Multiplication
# a = [[1,2,3],[4,5,6],[7,8,9]]
# b = [[6,4,8],[7,6,4],[3,6,9]]
# mat = []
# for r in range(len(a)):
#     line = []
#     for c in range(len(b[0])):
#         ele = 0
#         for k in range(len(b)):
#             ele += a[r][k] * b[k][c]
#         line.append(ele)
#     mat.append(line)
# print(mat)


# Transpose of a Matrix
# a = [[1,2,3],[4,5,6],[7,8,9]]
# tran = []
# for c in range(len(a[0])):
#     line = []
#     for r in range(len(a)):
#         line.append(a[r][c])
#     tran.append(line)
# print(tran)


# Frequency Count
# l = [1, 4, 2, 2, 1, 4, 6, 3]
# fre = {}
# for i in l:
#     fre[i] = fre.get(i, 0) + 1
# print(fre)


# Check if Array is Sorted
# l = [1, 2, 3, 4]
# b = all(l[i] <= l[i + 1] for i in range(len(l) - 1))
# print(b)


# Merge Two Lists
# a = [1, 2, 3]
# b = [4, 5, 3]
# print(a + b)


# Missing Number
# l = [0, 6, 2, 1, 4, 3]
# n = len(l) + 1
# total = n * (n + 1) // 2
# print(total - sum(l))


# Count Words in a String
# s = "I went to hyd"
# print(len(s.split()))


# Remove Spaces
# s = 'i am a super hero'
# print(s.replace(' ', ''))


# Find Duplicate Elements
# l = [1, 1, 2, 5, 2]
# s = set()
# for i in range(len(l)):
#     if l.count(l[i]) > 1:
#         s.add(l[i])
# print(list(s))


# Remove Duplicates from List
# l = [1, 4, 1, 2, 5, 2]
# a = []
# for i in l:
#     if i not in a:
#         a.append(i)
# print(a)


# Move All Zeros to End
# l = [1, 5, 0, 54, 0, 4]
# zeros = [i for i in l if i == 0]
# non_zeros = [i for i in l if i != 0]
# print(non_zeros + zeros)


# Rotate Array by 1 (Left)
# l = [1, 2, 3, 4, 5, 6]
# print(l[1:] + l[:1])


# Palindrome String Check
# s = "madamaa"
# print("palindrome" if s[::-1] == s else "not palindrome")


# Count Digits in a Number
# n = 1234
# print(len(str(n)))


# Smallest Element in List
# l = [6, 3, 8, 2, 4, 7]
# print(min(l))


# Right Angle Triangle Pattern
# num = 4
# for i in range(1, num + 1):
#     for j in range(1, i + 1):
#         print('*', end=' ')
#     print()


# Power of a Number
# n = 12
# print(n * n)


# Integer to Binary
# n = 8
# s, place = 0, 1
# while n > 0:
#     rem = n % 2
#     s += rem * place
#     n //= 2
#     place *= 10
# print(s)


# Binary to Integer
# n = 1000
# s, power = 0, 0
# while n > 0:
#     rem = n % 10
#     s += rem * (2 ** power)
#     n //= 10
#     power += 1
# print(s)


# Perfect Number
# n = 6
# c = sum(i for i in range(1, n) if n % i == 0)
# print("perfect" if c == n else "not")


# Strong Number
# n = 145
# dup = n
# s = 0
# while n > 0:
#     rem = n % 10
#     fact = 1
#     for i in range(1, rem + 1):
#         fact *= i
#     s += fact
#     n //= 10
# print("strong number" if s == dup else "not")


# Count Odd and Even in List
# l = [5, 3, 8, 4, 6, 2]
# co = sum(1 for i in l if i % 2 != 0)
# ce = sum(1 for i in l if i % 2 == 0)
# print("odd :", co, "even :", ce)


# Intersection of Two Arrays
# l1, l2 = [2, 4, 6, 8], [4, 3, 6, 1]
# print([i for i in l1 if i in l2])


# Check Substring
# s = "sundar raju is a good boy"
# sub = "good"
# print("substring is there" if sub in s else "not there")


# Remove Specific Character
# s = 'banana'
# print(s.replace('a', ''))


# Sum of Prime Numbers up to N
# n = 10
# s = 0
# for num in range(2, n + 1):
#     if all(num % i != 0 for i in range(2, num)):
#         s += num
# print(s)


# Reverse Words in a Sentence
# s = "hello all my name is sundar"
# print(" ".join(s.split()[::-1]))
# for word in s.split():
#     print(word[::-1], end=" ")
