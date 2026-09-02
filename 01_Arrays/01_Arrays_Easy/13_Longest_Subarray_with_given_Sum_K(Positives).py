# Problem: Longest Subarray With Sum K
# Approach: Sliding Window / Two Pointers
# TC: O(n)
# SC: O(1)

def longest_subarray(arr, k):
    left = 0
    current_sum = 0
    max_length = 0

    for right in range(len(arr)):
        current_sum += arr[right]

        if current_sum >= k:
            if current_sum == k:
                max_length = max(max_length, right - left + 1)

            current_sum -= arr[left]
            left += 1

    return max_length


arr = [10, 5, 2, 7, 1, 9]
k = 15

print(longest_subarray(arr, k))