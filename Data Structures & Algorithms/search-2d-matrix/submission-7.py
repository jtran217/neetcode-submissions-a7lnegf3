class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix)-1

        while top <= bottom:
            middleRow = (top + bottom)//2
            if target < matrix[middleRow][0]:
                bottom = middleRow-1
            elif target > matrix[middleRow][-1]:
                top = middleRow+1
            else:
                break
        
        row = (top + bottom) //2
        l,r = 0, len(matrix[0]) -1

        while l<=r:
            m = (l+r) //2
            if target > matrix[row][m]:
                l = m+1
            elif target < matrix[row][m]:
                r = m-1
            else:
                return True
        
        return False
