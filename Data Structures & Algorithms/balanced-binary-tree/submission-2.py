# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return (0,True)
            left = dfs(root.left)
            right = dfs(root.right)

            isValid = left[1] and right[1] and abs(left[0] - right[0]) <= 1

            return (max(left[0],right[0]) + 1, isValid)
        
        result = dfs(root)

        return result[1]


