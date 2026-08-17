# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # fast and slow pointers, if they ever meet return true
        slow = fast = head

        # while fast because it will reach end of list first
        # in the case that there's no cycle
        while fast and fast.next: 
            slow= slow.next
            fast= fast.next.next
            # if slow meets fast then there's a cycle
            if slow == fast: 
                return True
        #fast reaches end of list then while loop ends
        # no cycle return false 
        return False



        