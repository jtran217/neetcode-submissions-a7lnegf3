class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Find position of rotton food
        # BFS from there and keep track of time

        ROWS,COLS = len(grid),len(grid[0])
        visited = set()
        q = deque()
        fresh = 0
        def spread(r,c):
            nonlocal fresh
            if r<0 or c<0 or r==ROWS or c==COLS or grid[r][c] == 0:
                return
            visited.add((r,c))
            if grid[r][c] == 1:
                fresh-=1
                grid[r][c] = 2
                q.append((r,c))
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh+=1
                if grid[r][c] == 2:
                    q.append((r,c))
                    visited.add((r,c))
        time = 0
        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                spread(r+1,c)
                spread(r-1,c)
                spread(r,c+1)
                spread(r,c-1)
            time += 1
        
        return time if fresh ==0 else -1