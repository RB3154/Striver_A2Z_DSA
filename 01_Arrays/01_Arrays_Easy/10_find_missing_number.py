# Problem Statement:
# Given an array containing N-1 distinct integers from 1 to N,
# find the missing number.
#
# Example:
# Input:  [8, 2, 4, 5, 3, 7, 1]
# Output: 6
#
# ------------------------------------------------------------
# Approach 1: Naive - Sorting
# ------------------------------------------------------------
# Sort the array and find the first number that doesn't match
# its expected position.
#
# Time Complexity: O(N log N)
# Space Complexity: O(N) 
#
# ------------------------------------------------------------
# Approach 2: Better - Hashing
# ------------------------------------------------------------
# Use a hash/frequency array to mark the numbers present in
# the input array. The index with frequency 0 is the missing number.
#
# Time Complexity: O(N)
# Space Complexity: O(N)
#
# ------------------------------------------------------------
# Approach 3: Optimal 1 - Sum Formula
# ------------------------------------------------------------
# Calculate the sum of numbers from 1 to N using:
#
#     N * (N + 1) / 2
#
# Then subtract the sum of the elements in the array.
# The difference is the missing number.
#
# Time Complexity: O(N)
# Space Complexity: O(1)
#
# ------------------------------------------------------------
# Approach 4: Optimal 2 - XOR
# ------------------------------------------------------------
# XOR all numbers from 1 to N with all elements of the array.
#
# Since:
#     X ^ X = 0
#     X ^ 0 = X
#
# Every number that exists in both sets cancels out,
# leaving only the missing number.
#
# Time Complexity: O(N)
# Space Complexity: O(1)
#
# ------------------------------------------------------------


class X:
    def find_missing_num(self,arr):
        arr.sort()

        for i in range(1,len(arr)):
            if arr[i]!=arr[i-1]+1:
                return (arr[i-1]+arr[i])//2

    def find_missing_num_2(self,arr):
        n = len(arr)

        hash = [0] * (n + 2)

        for i in range(n):
            hash[arr[i]] += 1

        for i in range(1, n):
            if hash[i] == 0:
                return i

    def find_missing_num_3(self,arr):
        x=max(arr)
        return (x*(x+1))//2-sum(arr)

    def find_missing_num_4(self,arr):
        n = len(arr)+1
        xor1 = 0
        xor2 = 0

        for i in range(n - 1):
            xor2 ^= arr[i]

        for i in range(1, n + 1):
            xor1 ^= i

        return xor1 ^ xor2
    
x = X()
arr = [8, 2, 4, 5, 3, 7, 1]
print(x.find_missing_num_1(arr))