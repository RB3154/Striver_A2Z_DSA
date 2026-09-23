class Solution:

    # BRUTE FORCE
    # TC: O(n^2)
    # SC: O(1)
    def majorityElement_brute(self, nums):
        threshold = len(nums) // 2

        for candidate in nums:
            frequency = 0

            for value in nums:
                if value == candidate:
                    frequency += 1

            if frequency > threshold:
                return candidate

        return -1


    # BETTER
    # TC: O(n)
    # SC: O(k)
    def majorityElement_better(self, nums):
        threshold = len(nums) // 2
        frequencies = {}

        for value in nums:
            frequencies[value] = frequencies.get(value, 0) + 1

            if frequencies[value] > threshold:
                return value

        return -1


    # OPTIMAL
    # TC: O(n)
    # SC: O(1)
    def majorityElement_optimal(self, nums):
        candidate = 0
        balance = 0

        for value in nums:
            if balance == 0:
                candidate = value

            if value == candidate:
                balance += 1
            else:
                balance -= 1

        return candidate


sol = Solution()

nums = [2, 3, 2, 3, 3, 1, 3, 3]

print(sol.majorityElement_brute(nums))
print(sol.majorityElement_better(nums))
print(sol.majorityElement_optimal(nums))