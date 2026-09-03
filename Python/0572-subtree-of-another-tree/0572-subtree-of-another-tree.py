# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSame(self, root, subRoot):
        if root and subRoot:
            if root.val == subRoot.val: 
                return self.isSame(root.left, subRoot.left) and self.isSame(root.right, subRoot.right)
            return False
        return root is subRoot

    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """

        if root:
            if root.val == subRoot.val:
                if self.isSame(root, subRoot): 
                    return True
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        return False
        