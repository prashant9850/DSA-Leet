class Solution(object):
    def fourSum(self, arr, target):
        arr.sort()
        n = len(arr)
        ans = []

        for i in range(n - 3):

            # Skip duplicate i
            if i > 0 and arr[i] == arr[i - 1]:
                continue

            for j in range(i + 1, n - 2):

                # Skip duplicate j
                if j > i + 1 and arr[j] == arr[j - 1]:
                    continue

                k = j + 1
                l = n - 1

                while k < l:
                    s = arr[i] + arr[j] + arr[k] + arr[l]

                    if s < target:
                        k += 1

                    elif s > target:
                        l -= 1

                    else:
                        ans.append([arr[i], arr[j], arr[k], arr[l]])

                        k += 1
                        l -= 1

                        # Skip duplicate k
                        while k < l and arr[k] == arr[k - 1]:
                            k += 1

                        # Skip duplicate l
                        while k < l and arr[l] == arr[l + 1]:
                            l -= 1

        return ans