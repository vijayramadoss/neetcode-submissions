class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        s1 = {}
        s2 = {}
        s3 = {}

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                elif board[i][j] not in s1:
                    s1[board[i][j]] = 1
                else:
                    return False
            s1 = {}

            for j in range(len(board[i])):
                if board[j][i] == ".":
                    continue
                elif board[j][i] not in s2:
                    s2[board[j][i]] = 1
                else:
                    return False
            s2 = {}

        for i in range(0, len(board), 3):
            for j in range(0, len(board), 3):
                s3 = {}
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        if board[r][c] == ".":
                            continue
                        elif board[r][c] not in s3:
                            s3[board[r][c]] = 1
                        else:
                            return False

        return True