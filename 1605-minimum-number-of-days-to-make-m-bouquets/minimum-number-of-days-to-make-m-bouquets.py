class Solution(object):

    def possible(self, bloomDay, value, m, k):
        count = 0
        Bcount = 0

        for i in range(len(bloomDay)):

            if value >= bloomDay[i]:
                count += 1
            else:
                Bcount += count // k
                count = 0

        Bcount += count // k

        if Bcount >= m:
            return True
        else:
            return False

    def minDays(self, bloomDay, m, k):

        if m * k > len(bloomDay):
            return -1

        ans = -1
        low = min(bloomDay)
        high = max(bloomDay)

        while low <= high:

            mid = (low + high) // 2

            check = self.possible(bloomDay, mid, m, k)

            if check:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans