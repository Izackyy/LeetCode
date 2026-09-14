class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows, cols = len(board), len(board[0])

        def dfs(r, c, n):
            if n == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[n]:
                return False

            temp = board[r][c]
            board[r][c] = ''

            if dfs(r + 1, c, n + 1) or dfs(r - 1, c, n + 1) or dfs(r, c + 1, n + 1) or dfs(r, c - 1, n + 1):
                return True

            board[r][c] = temp
            return False

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        return False