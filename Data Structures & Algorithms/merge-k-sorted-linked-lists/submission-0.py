# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # if list doesn't exist
        if not lists or len(lists) == 0: 
            return None

        # while loop that runs until all lists have been merged into 1
        while len(lists) > 1:
            mergedLists= []
            # merge two lists at a time into the mergedLists variable above
            for i in range(0, len(lists), 2):
                l1= lists[i]
                l2= lists[i+1] if (i+1) < len(lists) else None #if list dne, default Null
                mergedLists.append(self.mergeList(l1, l2))
            lists= mergedLists # update lists to have the mergedLists so far

        return lists[0] # once all lists have been merged into one, return that list

    # function that does the merging 
    def mergeList(self, l1, l2):
        dummy= ListNode()
        tail= dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next= l1
                l1= l1.next
            else:
                tail.next= l2
                l2= l2.next
            tail= tail.next
        
        # add remaining list to end of tail 
        if l1:
            tail.next= l1
        elif l2:
            tail.next= l2
        
        return dummy.next # return entire list which will start at dummy.next

            
        