# ============================================================
# TOPIC: DSA — Linear Search
# ============================================================

# Iterative linear search
# l = [1, 4, 2, 7, 8, 4]
# t = 8
# for i in range(len(l)):
#     if l[i] == t:
#         print(i)
#         break
# else:
#     print(-1)

# Linear search using function
# def listindex(l, t, i=0):
#     if i >= len(l):
#         return -1
#     if l[i] == t:
#         return i
#     return listindex(l, t, i + 1)
#
# l = [1, 2, 3, 4, 3, 5, 2]
# t = 3
# print(listindex(l, t))


# ============================================================
# TOPIC: DSA — Binary Search
# ============================================================

# Iterative binary search
# l = [1, 5, 2, 7, -1, 6, 3, -5]
# l.sort()
# t = 7
# low, high = 0, len(l) - 1
# while low <= high:
#     mid = (low + high) // 2
#     if l[mid] > t:
#         high = mid - 1
#     elif l[mid] < t:
#         low = mid + 1
#     else:
#         print(mid)
#         break
# else:
#     print(-1)

# Recursive binary search
# def bsa(l, t, low, high):
#     if low > high:
#         return -1
#     mid = (low + high) // 2
#     if l[mid] == t:
#         return mid
#     elif l[mid] > t:
#         return bsa(l, t, low, mid - 1)
#     else:
#         return bsa(l, t, mid + 1, high)
#
# l = [1, 5, 2, 7, -1, 6, 3, -5]
# l.sort()
# t = 1
# print(bsa(l, t, 0, len(l) - 1))


# ============================================================
# TOPIC: DSA — Interpolation Search
# ============================================================

# l = [-3, -1, 3, 6, 7, 9, 12]
# t = 7
# low, high = 0, len(l) - 1
# while low <= high and l[low] <= t <= l[high]:
#     mid = int(low + ((high - low) / (l[high] - l[low])) * (t - l[low]))
#     if l[mid] > t:
#         high = mid - 1
#     elif l[mid] < t:
#         low = mid + 1
#     else:
#         print(mid)
#         break
# else:
#     print(-1)


# ============================================================
# TOPIC: DSA — Bubble Sort
# ============================================================

# l = [4, 8, 2, 4, 5, 1, 9]
# for i in range(len(l) - 1):
#     for j in range(len(l) - i - 1):
#         if l[j] > l[j + 1]:
#             l[j], l[j + 1] = l[j + 1], l[j]
# print(l)


# ============================================================
# TOPIC: DSA — Selection Sort
# ============================================================

# l = [3, 6, 2, 8, 4, 7]
# for i in range(len(l) - 1):
#     least = i
#     for j in range(i + 1, len(l)):
#         if l[least] > l[j]:
#             least = j
#     l[i], l[least] = l[least], l[i]
# print(l)


# ============================================================
# TOPIC: DSA — Quick Sort (Recursive)
# ============================================================

def quick_sort(l):
    if len(l) <= 1:
        return l
    pivot = l[0]
    left = [ele for ele in l[1:] if ele < pivot]
    right = [ele for ele in l[1:] if ele >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


l = [5, 7, -1, 4, 9, 0, 4, -5]
print(quick_sort(l))
