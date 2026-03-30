# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        fliped_root = recursive_flip(root)
        return fliped_root
    
def recursive_flip(node):
    if not node:
        return None
    if node.left == None and node.right == None:
        return node
    
    left_side = recursive_flip(node.left)
    right_side = recursive_flip(node.right)

    node.left = right_side
    node.right = left_side

    return node
        


        