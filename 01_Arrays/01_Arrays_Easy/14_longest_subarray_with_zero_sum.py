class longest_subarray_with_negatives:
    # BRUTE FORCE
    # TC = O(N^2)
    # SC = O(1)
    def longest_subarray(self,arr):
        max_len=0

        for i in range(len(arr)):
            cur_sum=0

            for j in range(i,len(arr)):
                cur_sum+=arr[j]

                if cur_sum==0:
                    max_len=max(max_len,j-i+1)

        return max_len

    # OPTIMAL 
    # TC = O(N)
    # SC = O(N)
    def longest_subarray_2(self,arr):
        max_len=0
        prefix_sum=0
        prefix_sum_freq={}

        for i,value in enumerate(arr):
            prefix_sum+=value

            if prefix_sum==0:
                max_len=max(max_len,i+1)

            elif prefix_sum in prefix_sum_freq:
                max_len=max(max_len,i-prefix_sum_freq[prefix_sum])

            else:
                prefix_sum_freq[prefix_sum]=i

        return max_len

x=longest_subarray_with_negatives()

arr = [9, -3, 3, -1, 6, -5]
print(x.longest_subarray_2(arr))

