# ============================================================
# TOPIC: Problem Solving — Minimum Swaps to Group Parities
# ============================================================

def minswap(arr):
    def cop(arr, parityfirst):
        swaps = 0
        pos = 0
        for i in range(len(arr)):
            if arr[i] % 2 == parityfirst:
                swaps = swaps + abs(i - pos)
                pos += 1
        return swaps
    odd_first = cop(arr, 1)
    even_first = cop(arr, 0)
    return min(odd_first, even_first)

n = int(input().strip())
arr = list(map(int, input().strip().split()))
print(minswap(arr))


# ============================================================
# TOPIC: Problem Solving — Rotate Array by K
# ============================================================

def rotate(nums, k):
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]
    return nums

print(rotate([1, 4, 6, 3, 7, 4], 2))


# ============================================================
# TOPIC: Problem Solving — Move Zeros to End
# ============================================================

def z(nums, p=0):
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[p], nums[i] = nums[i], nums[p]
            p += 1
    return nums

print(z([1, 0, 4, 3, 0]))


# ============================================================
# TOPIC: Problem Solving — Find Maximum Element
# ============================================================

def s(n):
    n.sort(reverse=True)
    return n[0]

print(s([5, 2, 9, 5, 3]))
