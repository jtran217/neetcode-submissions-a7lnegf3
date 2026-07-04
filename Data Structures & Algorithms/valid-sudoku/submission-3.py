class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = defaultdict(list)
        colSet = defaultdict(list)
        cubeSet = defaultdict(list)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rowSet[r] or  board[r][c] in colSet[c] or board[r][c] in cubeSet[(r//3,c//3)]:
                    return False
                rowSet[r].append(board[r][c])
                colSet[c].append(board[r][c])
                cubeSet[(r//3,c//3)].append(board[r][c])
        
        return True