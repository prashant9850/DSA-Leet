class Solution:
    def mergeOverlap(self, arr):
        arr.sort()
        ans = []

        for i in range(len(arr)):
            start = arr[i][0]
            end = arr[i][1]

            if ans and end <= ans[-1][1]:
                continue

            for j in range(i + 1, len(arr)):
                if arr[j][0] <= end:
                    end = max(end, arr[j][1])
                else:
                    break

            ans.append([start, end])

        return ans