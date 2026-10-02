class Solution(object):
    def singleNonDuplicate(self, nums):

        low = 0
        high = len(nums) - 1

        while low < high:

            mid = (low + high) // 2

            # Make mid even
            if mid % 2 == 1:
                mid -= 1

            # Correct pair -> single element is on the right
            if nums[mid] == nums[mid + 1]:
                low = mid + 2

            # Incorrect pair -> single element is on the left
            else:
                high = mid

        return nums[low]