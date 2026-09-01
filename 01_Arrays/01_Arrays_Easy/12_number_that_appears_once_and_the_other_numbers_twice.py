"""
Problem: Single Element in an Array

Given an array where every element appears twice except one element,
find and return the element that appears only once.

Example:
arr = [4, 1, 2, 1, 2]
Answer = 4
"""


# ============================================================
# 1. BRUTE FORCE APPROACH
# ============================================================

def brute_force(arr):
    n = len(arr)

    for i in range(n):
        num = arr[i]
        count = 0

        for j in range(n):
            if arr[j] == num:
                count += 1

        if count == 1:
            return num

    return -1


# TC: O(n^2)
# SC: O(1)


# ============================================================
# 2. BETTER APPROACH: FREQUENCY HASHING
# ============================================================

def better_hashing(arr):
    if not arr:
        return -1

    maxi = max(arr)

    hash_arr = [0] * (maxi + 1)

    for num in arr:
        hash_arr[num] += 1

    for num in arr:
        if hash_arr[num] == 1:
            return num

    return -1


# TC: O(n + max(arr))
# SC: O(max(arr))


# ============================================================
# 3. OPTIMAL APPROACH: XOR
# ============================================================

def optimal_xor(arr):
    xorr = 0

    # Duplicate numbers cancel each other:
    # a ^ a = 0
    # a ^ 0 = a
    for num in arr:
        xorr ^= num

    return xorr


# TC: O(n)
# SC: O(1)


arr = [4, 1, 2, 1, 2]

print("Array:", arr)

print("Brute Force:", brute_force(arr))
print("Better:", better_hashing(arr))
print("Optimal:", optimal_xor(arr))