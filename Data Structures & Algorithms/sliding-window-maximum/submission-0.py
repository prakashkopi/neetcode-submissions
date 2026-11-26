class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans= []
        dq= deque() # index
        l = r = 0

        # nums= [1,2,1,0,4,2,6], k = 3

        while r < len(nums):
            while dq and nums[dq[-1]] < nums[r]: 
                dq.pop()
            dq.append(r)

            if l > dq[0]: 
                dq.popleft()
            
            if (r+1) >= k: 
                ans.append(nums[dq[0]])
                l+= 1
            r += 1
        
        return ans


