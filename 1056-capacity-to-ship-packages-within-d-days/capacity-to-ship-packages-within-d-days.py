class Solution(object):
    def check(self,weights,days,capacity):
        total=0
        count=1
        for weight in weights:

            if total + weight > capacity:
                count += 1
                total = weight
            else:
                total += weight
        return count<=days
    def shipWithinDays(self, weights, days):
        ans=0
        low=max(weights)
        high=sum(weights)
        while(low<=high):
            mid=(low+high)//2
            check=self.check(weights,days,mid)
            if (check==True):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
        
        