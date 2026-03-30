class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # iteratre through each row and col
        # dfs from that char
        # if char matches continue if not return.

        # Set store position

        visited = set()

        def findWord(r, c, board, visited, word):
            if len(word) == 0:       
                return True
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                return False
            if (r, c) in visited:
                return False
            if board[r][c] != word[0]:
                return False
            
            visited.add((r, c))

            found = (findWord(r-1, c, board, visited, word[1:]) or
                    findWord(r+1, c, board, visited, word[1:]) or
                    findWord(r, c-1, board, visited, word[1:]) or
                    findWord(r, c+1, board, visited, word[1:]))

            visited.remove((r, c))     # ← backtrack!

            return found


        for r in range(len(board)):
            for c in range(len(board[0])):
                if findWord(r,c,board,visited,word):
                    return True
        return False

