# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        #checker is the running total
        def helper(root, targetSum, checker):
            if root is not None:
                print(root.val)
                if root.right is None and root.left is None:
                    checker+=root.val
                    return targetSum==checker
                if root.left is not None and root.right is not  None:
                    return helper(root.left,targetSum,checker+root.val) or helper(root.right,targetSum,checker+root.val)
                elif root.left is not None and root.right is None:
                    return helper(root.left,targetSum,checker+root.val)
                elif root.left is None and root.right is not None:
                    return helper(root.right,targetSum,checker+root.val)
        return helper(root, targetSum,0)
