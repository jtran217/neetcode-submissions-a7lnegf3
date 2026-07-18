class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top,bottom = 0, len(matrix) - 1
        
        while top <= bottom:
            row = (bottom + top) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break
        row = (bottom + top) // 2 
        l,r = 0, len(matrix[0]) - 1
        while l<=r:
            m = (l+r) // 2
            if target == matrix[row][m]:
                return True
            if target >  matrix[row][m]:
                l = m + 1
            else:
                r = m - 1
        
        
        return False
