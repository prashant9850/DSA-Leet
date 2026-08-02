class Solution(object):
    #ggg
    def threeSum(self, nums):
        ans=[]
        nums.sort()
        i=0
        while i<len(nums)-2:
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            j=i+1
            k=len(nums)-1
            while j<k:
                if (nums[i]+nums[j]+nums[k])>0:
                    k-=1
                elif (nums[i]+nums[j]+nums[k])<0:
                    j+=1
                else:
                    triplet=[nums[i],nums[j],nums[k]]
                    
                    ans.append(triplet)
                    j += 1
                    k -= 1

                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
            i+=1
        return ans

        