class Solution:
    def subarrayXor(self, arr, m):
        prefix = 0
        count = 0

        freq = {0: 1}      # Prefix XOR 0 occurs once initially

        for num in arr:
            prefix ^= num

            count += freq.get(prefix ^ m, 0)

            freq[prefix] = freq.get(prefix, 0) + 1

        return count