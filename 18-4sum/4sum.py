class Solution(object):
    def fourSum(self, nums, target):
        n = len(nums)
        ans = set()

        for i in range(n):
            for j in range(i + 1, n):
                seen = set()

                for k in range(j + 1, n):
                    need = target - (nums[i] + nums[j] + nums[k])

                    if need in seen:
                        quad = tuple(sorted([nums[i], nums[j], nums[k], need]))
                        ans.add(quad)

                    seen.add(nums[k])

        return [list(x) for x in ans]