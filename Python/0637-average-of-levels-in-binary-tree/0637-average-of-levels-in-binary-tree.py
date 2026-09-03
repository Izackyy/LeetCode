# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """

        if not root: return []
        ans, q = [], deque([root])

        while q:
            levelSum = 0
            count = len(q)

            for _ in range(count):
                node = q.popleft()
                levelSum += node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

            ans.append(float(levelSum) / count)
        
        return ans