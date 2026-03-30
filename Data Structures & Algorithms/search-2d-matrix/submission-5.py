class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Two binary search, one done on row then one on column.
        # If target > matrix[row][-1] increment top because the target is in next row
        # If target < matrix[row][0] decrement bottom because target is in row above.

        ROW, COL = len(matrix),len(matrix[0])
        top,bot = 0, ROW-1

        while top <= bot:
            row = (top + bot) // 2

            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        
        if  (top > bot):
            return False
        row = (top + bot) // 2 
        l,r = 0, COL-1

        while l <= r:
            m = (l + r) //2
            if matrix[row][m] == target:
                return True
            if target > matrix[row][m]:
                l = m+1
            else:
                r = m - 1
        return False