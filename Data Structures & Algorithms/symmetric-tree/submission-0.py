# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # base case - empty tree is considered symmetric
        if not root: return True

        # bfs - check by level
        q= deque([(root.left, root.right)])

        while q:
            for _ in range(len(q)):            
                left, right= q.popleft()

                # if either is null, continue
                if not left and not right: 
                    continue
                
                if not left or not right or left.val != right.val: 
                    return False

                q.append((left.left, right.right))
                q.append((left.right, right.left))
        
        return True
            







        