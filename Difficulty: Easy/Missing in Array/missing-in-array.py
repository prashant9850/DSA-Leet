class Solution:
    def missingNum(self, arr):
        n = len(arr)

        sum1 = (n + 1) * (n + 2) // 2
        sum2 = sum(arr)

        return sum1 - sum2