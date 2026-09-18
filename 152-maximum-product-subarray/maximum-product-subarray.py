class Solution(object):
    def maxProduct(self, nums):
        ans = nums[0]
        pre = 1
        suf = 1
        n = len(nums)

        for i in range(n):
            pre = pre * nums[i]
            suf = suf * nums[n - i - 1]

            ans = max(ans, pre, suf)

            if pre == 0:
                pre = 1

            if suf == 0:
                suf = 1

        return ans