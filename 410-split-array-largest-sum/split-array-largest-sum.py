class Solution(object):

    def check(self, nums, k, mid):
        total = 0
        count = 1

        for i in range(len(nums)):
            if total + nums[i] > mid:
                count += 1
                total = nums[i]
            else:
                total += nums[i]

        return count <= k

    def splitArray(self, nums, k):
        ans = 0
        low = max(nums)
        high = sum(nums)

        while low <= high:
            mid = (low + high) // 2

            check = self.check(nums, k, mid)

            if check == True:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans