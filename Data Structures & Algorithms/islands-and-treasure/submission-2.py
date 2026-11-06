class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()
        q = deque()
        ROWS,COLS = len(grid),len(grid[0])

        def traverse(r,c):
            if r<0 or r==ROWS or c<0 or c==COLS or grid[r][c] == -1 or (r,c) in visited:
                return
            visited.add((r,c))
            q.append((r,c))
        # Find treasure and store in queue 
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    visited.add((r,c))
                    q.append((r,c))
        
        # Perform BFS replace spots with distance
        distance = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = distance

                traverse(r+1,c)
                traverse(r-1,c)
                traverse(r,c+1)
                traverse(r,c-1)
            distance += 1
