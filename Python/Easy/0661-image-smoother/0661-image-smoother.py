class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        r = len(img)
        c = len(img[0])

        ans = [[0] * c for _ in range(r)]

        for i in range(r):
            for j in range(c):
                total = 0
                count = 0

                for x in (i - 1, i, i + 1):
                    for y in (j - 1, j, j + 1):
                        if 0 <= x < r and 0 <= y < c:
                            total += img[x][y]
                            count += 1

                ans[i][j] = total / count

        return ans