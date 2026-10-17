
class Solution(object):
    def searchMatrix(self, matrix, target):
        rows = len(matrix)
        cols = len(matrix[0])

        low = 0
        high = rows - 1

        while low <= high:
            mid = (low + high) // 2

            if matrix[mid][0] <= target <= matrix[mid][cols - 1]:
                low2 = 0
                high2 = cols - 1

                while low2 <= high2:
                    mid2 = (low2 + high2) // 2

                    if matrix[mid][mid2] == target:
                        return True

                    elif target > matrix[mid][mid2]:
                        low2 = mid2 + 1

                    else:
                        high2 = mid2 - 1

                return False

            elif target > matrix[mid][cols - 1]:
                low = mid + 1

            else:
                high = mid - 1

        return False

