class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        visited = set()
        ROWS,COLS = len(grid),len(grid[0])

        def dfs(r,c):
            if r<0 or c<0 or r >= ROWS or c >= COLS or grid[r][c] == 0 or (r,c) in visited:
                return 0
            
            visited.add((r,c))
            currentArea = 1

            currentArea += dfs(r+1,c)
            currentArea += dfs(r-1,c)
            currentArea += dfs(r,c+1)
            currentArea += dfs(r,c-1)

            return currentArea
        
        for r in range(ROWS):
            for c in range(COLS):
                currentIsland = dfs(r,c)
                maxArea = max(currentIsland,maxArea)
        
        return maxArea