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
                return [0,True]
            leftVal = dfs(root.left)
            rightVal = dfs(root.right)

            balanced = abs(leftVal[0] - rightVal[0]) <= 1 and leftVal[1] and rightVal[1]

            return (max(leftVal[0],rightVal[0]) + 1, balanced)
        res = dfs(root)
        return res[1]
            

