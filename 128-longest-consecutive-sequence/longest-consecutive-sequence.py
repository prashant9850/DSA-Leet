class Solution(object):
    def longestConsecutive(self, nums):
        
        if len(nums) == 0:
            return 0

        longest = 1

        # Create a set containing all elements
        st = set(nums)

        # Traverse through the set
        for num in st:

            # Check if num is the starting element
            if num - 1 not in st:

                cnt = 1
                x = num

                # Find consecutive elements
                while x + 1 in st:
                    x = x + 1
                    cnt = cnt + 1

                longest = max(longest, cnt)

        return longest