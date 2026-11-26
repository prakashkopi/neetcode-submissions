class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans= []
        dq= deque() # index
        l = r = 0

        # nums= [1,2,1,0,4,2,6], k = 3
        while r < len(nums):
            # pop smaller values from the queue
            while dq and nums[dq[-1]] < nums[r]: 
                dq.pop()
            dq.append(r)

            # remove left val from window if 
            # leftmost value in queue is < l pointer
            if dq[0] < l: 
                dq.popleft()
            
            # once window is size k, append max to answer and 
            # shrink window by moving the left pointer
            # max will always be the leftmost index in our queue
            if (r - l + 1) == k: 
                ans.append(nums[dq[0]])
                l+= 1
            r += 1
        
        return ans


