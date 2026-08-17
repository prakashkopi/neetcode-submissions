class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # don't need to use linked list for this problem
        # but we will use the tortoise and hare algorithm --> O(n) time, O(1) space
        slow = fast = nums[0]
        
        # moves pointers to end of list
        while True:
            slow= nums[slow]
            fast= nums[nums[fast]]
            if slow == fast:
                break

        # find intersection (will eventually equal the same)
        slow2= nums[0]
        while slow2 != slow:
            slow2= nums[slow2]
            slow= nums[slow]
        
        return slow






        