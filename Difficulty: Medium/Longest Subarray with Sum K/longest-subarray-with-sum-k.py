class Solution:
    def longestSubarray(self, arr, k):  
        current_sum=0
        hashmap={}
        max_len=0
        for i in range(len(arr)):
            current_sum=current_sum+arr[i]
            if (current_sum==k):
                max_len=max(max_len,i+1)
            temp=current_sum-k
            if temp in hashmap:
                max_len=max(max_len,i-hashmap[temp])
            if current_sum not in hashmap:
                hashmap[current_sum]=i
        return max_len
            
    
