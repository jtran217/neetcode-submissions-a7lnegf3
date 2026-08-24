class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if self.findIsland(grid,r,c,visited):
                    count += 1
        return count

    def findIsland(self,grid,row,col,visited):
        if not 0 <= row < len(grid)  or not 0 <= col < len(grid[0]):
            return False
        pos = grid[row][col]
        if (row,col) in visited:
            return False
        if pos == "0":
            return False
        visited.add((row,col))

        self.findIsland(grid,row+1,col,visited)
        self.findIsland(grid,row-1,col,visited)
        self.findIsland(grid,row,col+1,visited)
        self.findIsland(grid,row,col-1,visited)

        return True

