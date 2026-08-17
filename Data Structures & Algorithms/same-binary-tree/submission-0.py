# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # base cases
        if not p and not q: # if neither tree exists
            return True
        if not p or not q or p.val != q.val: # if one doesn't exist, or they both exist but values don't match
            return False
        
        # return True if left val == right val else False
        return (self.isSameTree(p.left, q.left)
        and self.isSameTree(p.right, q.right))

    
        