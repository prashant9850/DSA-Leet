class Solution:
    def findTwoElement(self, arr):
        n = len(arr)

        Sn = (n * (n + 1)) // 2
        S2n = (n * (n + 1) * (2 * n + 1)) // 6

        S = 0
        S2 = 0

        for i in range(len(arr)):
            S = S + arr[i]
            S2 = S2 + (arr[i] * arr[i])

        val1 = S - Sn
        val2 = S2 - S2n

        val2 = val2 // val1

        X = (val1 + val2) // 2
        Y = X - val1

        return (X, Y)