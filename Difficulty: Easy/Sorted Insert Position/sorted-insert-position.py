class Solution:
    def searchInsertK(self, arr, k):
        n=len(arr)
        ans=n
        low=0
        high=n-1
        while (low<=high):
            mid=(low+high)//2
            if (arr[mid]>=k):
                ans=mid
                high=mid-1
            else:
                low=mid+1

        return ans
        