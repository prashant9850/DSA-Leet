class Solution(object):
    def findMin(self, nums):
        ans = float('inf')

        low = 0
        high = len(nums) - 1

        while low <= high:
            # If current portion is already sorted
            if nums[low] <= nums[high]:
                ans = min(ans, nums[low])
                break

            mid = (low + high) // 2

            # Left half is sorted
            if nums[low] <= nums[mid]:
                ans = min(ans, nums[low])
                low = mid + 1

            # Right half is sorted
            else:
                ans = min(ans, nums[mid])
                high = mid - 1

        return ans