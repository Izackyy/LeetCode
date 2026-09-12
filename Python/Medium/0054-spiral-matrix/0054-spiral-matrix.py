class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        r_start, r_end = 0, len(matrix)
        c_start, c_end = 0, len(matrix[0])
        ans = []

        while (r_start < r_end) and (c_start < c_end):
            for i in range(c_start, c_end):  # top row
                ans.append(matrix[r_start][i])

            for j in range(r_start + 1, r_end):  # right col
                ans.append(matrix[j][c_end - 1])

            if r_start + 1 < r_end:
                for i in range(c_end - 2, c_start - 1, -1):  # btm row
                    ans.append(matrix[r_end - 1][i])

            if c_start + 1 < c_end:
                for j in range(r_end - 2, r_start, -1):  # left col
                    ans.append(matrix[j][c_start])
        
            r_start += 1
            r_end -= 1
            c_start += 1
            c_end -= 1

        return ans