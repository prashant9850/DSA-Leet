class Solution(object):
    def findKthPositive(self, arr, k):

        count = k
        ans = 1
        i = 1
        j = 0

        while i <= max(arr):

            if j < len(arr) and arr[j] == i:
                i += 1
                j += 1

            else:
                count -= 1
                ans = i

                if count == 0:
                    return ans

                i += 1

        # If kth missing number is after max(arr)
        while count > 0:
            count -= 1
            ans = i
            i += 1

        return ans