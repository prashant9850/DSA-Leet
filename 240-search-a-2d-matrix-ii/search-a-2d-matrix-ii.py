class Solution(object):
    def searchMatrix(self, matrix, target):
        row=0
        column=len(matrix[0])-1
        while (row<len(matrix) and column>=0):
            if (matrix[row][column]==target):
                return True
                break
            elif (matrix[row][column]>target):
                column-=1
            else:
                row+=1
        return False
        