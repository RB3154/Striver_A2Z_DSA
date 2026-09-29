# Problem: Leaders in an Array

class LeadersInArray:

    # 1. BRUTE FORCE APPROACH
    # TC: O(n^2)
    # SC: O(1) auxiliary space, excluding the output list

    def leaders_brute(self, arr):
        n = len(arr)
        leaders = []

        for i in range(n):
            is_leader = True

            for j in range(i + 1, n):
                if arr[j] >= arr[i]:
                    is_leader = False
                    break

            if is_leader:
                leaders.append(arr[i])

        return leaders

    # 2. BETTER APPROACH: SUFFIX MAXIMUM ARRAY
    # TC: O(n)
    # SC: O(n) auxiliary space for the suffix_max array,excluding the output list  

    def leaders_better(self, arr):
        n = len(arr)

        if n == 0:
            return []

        leaders = []
        suffix_max = [0] * n

        # Build suffix maximums from right to left.
        suffix_max[n - 1] = arr[n - 1]

        for i in range(n - 2, -1, -1):
            suffix_max[i] = max(arr[i], suffix_max[i + 1])

        # Compare each element with the maximum to its right.
        for i in range(n):
            if i == n - 1 or arr[i] > suffix_max[i + 1]:
                leaders.append(arr[i])

        return leaders
 
    # 3. OPTIMAL APPROACH: RUNNING MAXIMUM
    # TC: O(n)
    # SC: O(1) auxiliary space, excluding the output list

    def leaders_optimal(self, arr):
        n = len(arr)

        if n == 0:
            return []

        leaders = []
        max_right = arr[n - 1]
        leaders.append(max_right)

        # Traverse from right to left, maintaining the maximum.
        for i in range(n - 2, -1, -1):
            if arr[i] > max_right:
                leaders.append(arr[i])
                max_right = arr[i]

        # Leaders were collected in reverse order.
        leaders.reverse()

        return leaders

arr = [10, 22, 12, 3, 0, 6]

obj = LeadersInArray()

print("Input:", arr)
print("Brute Force:", obj.leaders_brute(arr))
print("Better:", obj.leaders_better(arr))
print("Optimal:", obj.leaders_optimal(arr))
