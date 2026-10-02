class Solution(object):
    def mySqrt(self, x):
        ans=1
        low=1
        high=x
        if x==0:
            return 0
        while(low<=high):
            mid=(low+high)//2
            if (mid*mid>x):
                high=mid-1
            else:
                ans=max(ans,mid)
                low=mid+1
        return ans
        