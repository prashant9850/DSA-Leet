class Solution:
    def findCeil(self, arr, x):
        n=len(arr)
        low=0
        ans=-1
        high=n-1
        while(low<=high):
            mid=(low+high)//2
            if (arr[mid]>=x):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans