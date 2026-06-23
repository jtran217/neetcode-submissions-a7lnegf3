class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colSet = defaultdict(set)
        rowSet = defaultdict(set)
        squareSet = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                pos = board[r][c]

                if pos in rowSet[r] or pos in colSet[c] or pos in squareSet[(r//3),(c//3)]:
                    return False
                
                rowSet[r].add(pos)
                colSet[c].add(pos)
                squareSet[(r//3),(c//3)].add(pos)
        
        return True
