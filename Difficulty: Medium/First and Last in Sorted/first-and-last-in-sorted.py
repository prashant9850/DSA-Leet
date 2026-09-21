class Solution:
    def upperBound(self, arr, target):
        low = 0
        high = len(arr) - 1
        ans = len(arr)

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] > target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

    def lowerBound(self, arr, target):
        low = 0
        high = len(arr) - 1
        ans = len(arr)

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] >= target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

    def find(self, arr, x):
        lb = self.lowerBound(arr, x)

        if lb == len(arr) or arr[lb] != x:
            return [-1, -1]

        return [lb, self.upperBound(arr, x) - 1]