# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # [2,4,6,8]
        slow, fast= head, head.next

        # Get fast to end of list, slow to middle of list
        while fast and fast.next:
            slow= slow.next
            fast= fast.next.next

        # Second list will start at slow.next
        second= slow.next
        slow.next= None # We do this because we are splitting the lists into 2 
        # second will be [6,8] and first is [2,4]

        # reverse second half of list
        prev= None
        while second:
            tmp= second.next
            second.next= prev
            prev= second
            second= tmp
        
        # merge both lists
        first, second= head, prev
        while second: 
            tmp1, tmp2= first.next, second.next
            first.next= second
            second.next= tmp1
            first, second= tmp1, tmp2





        
        