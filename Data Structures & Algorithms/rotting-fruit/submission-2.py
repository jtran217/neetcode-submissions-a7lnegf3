class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid),len(grid[0])
        q = deque()
        fresh = 0
        # Find number of fresh banana and starting position of rotton banana
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r,c))
        
        time = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()

                for dr,dc in directions:
                    nr,nc = r + dr, c + dc
                    if (nr in range(len(grid)) and nc in range(len(grid[0])) and grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        q.append((nr,nc))
                        fresh -= 1
            time += 1
        
        return time if fresh ==0 else -1 

