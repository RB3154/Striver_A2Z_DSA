# Problem: Union of Two Sorted Arrays
#
# Time Complexity: O(n + m)
# Space Complexity: O(n + m)

class Solution:
    def find_union(self,arr1,arr2):
        union=[]
        i=j=0

        def add(x):
            if not union or union[-1]!=x:
                union.append(x)

        while i<len(arr1) and j<len(arr2):
            if arr1[i]<arr2[j]:
                add(arr1[i])
                i+=1

            elif arr2[j]<arr1[i]:
                add(arr2[j])
                j+=1

            else:
                add(arr1[i])
                i+=1
                j+=1

        while i<len(arr1):
            add(arr1[i])
            i+=1

        while j<len(arr2):
            add(arr2[j])
            j+=1

        return union

x=Solution()
a=[1,2,3,3,4,5]
b=[2,3,4,5,6,7,7]
print(x.find_union(a,b))