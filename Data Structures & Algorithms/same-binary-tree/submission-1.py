# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pq= deque([p])
        qq= deque([q])

        while pq and qq: 
            nodeP= pq.popleft()
            nodeQ= qq.popleft()

            # if null do nothing and continue to next iter
            if nodeP is None and nodeQ is None: 
                continue
            
            # if either node is null or values don't match 
            if nodeP is None or nodeQ is None or nodeP.val != nodeQ.val:
                return False
            
            pq.append(nodeP.left)
            pq.append(nodeP.right)
            qq.append(nodeQ.left)
            qq.append(nodeQ.right)
        
        return True 
            


        