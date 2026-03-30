class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = defaultdict(set)
        col_set = defaultdict(set)
        square_set = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                pos = board[r][c]

                if (pos in row_set[r] or pos in col_set[c] or pos in square_set[(r//3,c//3)]):
                    return False
                
                row_set[r].add(pos)
                col_set[c].add(pos)
                square_set[(r//3,c//3)].add(pos)

        return True