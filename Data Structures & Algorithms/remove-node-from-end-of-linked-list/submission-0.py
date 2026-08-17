# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy= ListNode()
        dummy.next = head
        behind = ahead = dummy

        # move ahead pointer to n+1 position
        for _ in range(n+1):
            ahead= ahead.next

        # once ahead pointer goes out of bounds, behind will be at nth node
        while ahead:
            behind= behind.next
            ahead= ahead.next

        # remove nth node by skipping it
        behind.next= behind.next.next
        return dummy.next
        

        
        
            

        
    
        
    


        


        