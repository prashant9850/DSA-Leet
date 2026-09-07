class Solution(object):
    def merge(self, nums1, m, nums2, n):
        ans=[]
        i=0
        j=0
        while(i<m and j<n):
            if (nums1[i]<nums2[j]):
                ans.append(nums1[i])
                i+=1
            elif (nums1[i]>nums2[j]):
                ans.append(nums2[j])
                j+=1
            else:
                ans.append(nums1[i])
                ans.append(nums2[j])
                i+=1
                j+=1
        while(i<m):
            ans.append(nums1[i])
            i+=1
        while(j<n):
            ans.append(nums2[j])
            j+=1
        for i in range(m + n):
            nums1[i] = ans[i]


        