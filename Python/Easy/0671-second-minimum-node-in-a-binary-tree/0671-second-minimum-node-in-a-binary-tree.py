# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object): 

    def findSecondMinimumValue(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        ans = [float('inf'), float('inf')]

        def dfs(node):
            if not node: return

            if node.val < ans[0]:
                ans[1] = ans[0]
                ans[0] = node.val
            elif ans[0] < node.val < ans[1]:
                ans[1] = node.val

            dfs(node.left)
            dfs(node.right) 

        dfs(root)

        if ans[1] == float('inf'): return -1
        
        return ans[1]


