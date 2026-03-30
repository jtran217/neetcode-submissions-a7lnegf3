class Solution:
    def findIsland(self,r,c,seen,grid):
        rowInbound = 0<= r < len(grid)
        colInbound = 0 <= c < len(grid[0])
        if not rowInbound or not colInbound:
            return False
        if grid[r][c] == '0':
            return False
        pos = (r,c)
        if  pos in seen:
            return False
        seen.add(pos)
        self.findIsland(r+1,c,seen,grid)
        self.findIsland(r-1,c,seen,grid)
        self.findIsland(r,c+1,seen,grid)
        self.findIsland(r,c-1,seen,grid)
        return True

    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        seen = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if self.findIsland(r,c,seen,grid) == True:
                    count += 1
        return count