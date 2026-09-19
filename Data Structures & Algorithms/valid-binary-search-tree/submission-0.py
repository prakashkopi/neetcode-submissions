# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val4
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # helper function to check both subtrees
        def valid(node, left, right):
            # base case, empty tree is considered valid
            if not node:
                return True
            if not (left < node.val < right):
                return False
            
            #both subtrees must be valid
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)
        
        # bounds will be updated by the dfs above
        return valid(root, float("-inf"), float("inf"))


        