class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    v = board[i][j]
                    if (v, i) in seen or (j, v) in seen or (i//3, j//3, v) in seen:
                        return False
                    seen |= {(v, i), (j, v), (i//3, j//3, v)}
        return True
