"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # store old to new copy in a hashmap
        oldToNew= {None : None} # initialize key-value pair to None to avoid error
        curr= head

        # add copies to hashmap
        while curr:
            copy= Node(curr.val)
            oldToNew[curr]= copy
            curr= curr.next

        # copy pointers over
        curr= head
        while curr:
            copy= oldToNew[curr]
            copy.next= oldToNew[curr.next]
            copy.random= oldToNew[curr.random]

            curr= curr.next
        
        return oldToNew[head]