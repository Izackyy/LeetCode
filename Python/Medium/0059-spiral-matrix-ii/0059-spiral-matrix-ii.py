class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        r_start, r_end = 0, n
        c_start, c_end = 0, n
        element = 1
        matrix = [[0] * n for _ in range(n)]

        while (r_start < r_end) and (c_start < c_end) and element <= n * n:
            for i in range(c_start, c_end):  # top row
                matrix[r_start][i] = element
                element += 1

            for j in range(r_start + 1, r_end):  # right col
                matrix[j][c_end - 1] = element
                element += 1

            for i in range(c_end - 2, c_start - 1, -1):  # btm row
                matrix[r_end - 1][i] = element
                element += 1

            for j in range(r_end - 2, r_start, -1):  # left col
                matrix[j][c_start] = element
                element += 1
        
            r_start += 1
            r_end -= 1
            c_start += 1
            c_end -= 1

        return matrix