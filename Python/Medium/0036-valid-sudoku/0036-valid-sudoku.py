class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [[False] * 9 for _ in range(9)]
        cols = [[False] * 9 for _ in range(9)]
        boxes = [[False] * 9 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = ord(board[i][j]) - ord('1') 
                    box_idx = (i // 3) * 3 + (j // 3)

                    if rows[i][num] or cols[num][j] or boxes[box_idx][num]:
                        return False
                    
                    rows[i][num] = cols[num][j] = boxes[box_idx][num] = True

        return True