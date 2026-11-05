class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()
        q = deque()
        ROWS,COLS = len(grid),len(grid[0])
        
        def traverse(r,c):
            if r<0 or r == ROWS or c < 0 or c == COLS or (r,c) in visited or grid[r][c] == -1:
                return
            visited.add((r,c))
            q.append((r,c))



        # Find all treasure position
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    visited.add((r,c))
                    q.append((r,c))
        # BFS from treasure
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

