# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True #if subRoot tree doesnt exist, we auto return true
        if not root: return False #if root tree doesnt exist, we can't possibly have an equal subRoot so return false
        
        # if subRoot is equal starting from root node, we return true
        if self.sameTree(root, subRoot):
            return True

        # if root doesn't equal subRoot, recursively call this function to see if root.left or root.right is equal to subTree
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    # this is a LC easy problem on it's own. It checks if two trees are equal by recursively checking their values
    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if both trees are empty, they are equal so we return true
        if not root and not subRoot: 
            return True
        
        # if both trees have matching values, check left and right subtrees recursively and check if they are also equal
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)) # returns true if both subtrees are equal
        return False # return false by default 

            
            
        
