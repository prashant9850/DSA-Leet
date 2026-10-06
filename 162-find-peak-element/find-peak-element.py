class Solution(object):
    def findPeakElement(self, nums):
        ans=0
        low=1
        high=len(nums)-1
        while(low<=high):
            mid=(low+high)//2
            if (nums[mid]>nums[mid-1]):
                ans=max(mid,ans)
                low=mid+1
            else:
                high=mid-1
        return ans
        