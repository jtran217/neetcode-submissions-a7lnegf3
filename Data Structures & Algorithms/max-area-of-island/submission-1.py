class Solution:
    def findArea(self,grid,r,c,visited):
        rBound = 0 <= r < len(grid)
        cBound = 0 <= c < len(grid[0])
        if not rBound or not cBound:
            return 0
        if grid[r][c] == 0:
            return 0
        pos = (r,c)
        if pos in visited:
            return 0
        visited.add(pos)
        area = 1
        area += self.findArea(grid,r+1,c,visited)
        area += self.findArea(grid,r-1,c,visited)
        area += self.findArea(grid,r,c+1,visited)
        area += self.findArea(grid,r,c-1,visited)

        return area



    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        mArea = 0
        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                islandArea = self.findArea(grid,r,c,visited)
                mArea = max(mArea,islandArea)
        return mArea
        