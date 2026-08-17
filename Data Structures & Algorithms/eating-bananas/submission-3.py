class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # O(log max(p) * p) time, O(n) space
        l, r= 1, max(piles)
        res= r #initialize to largest amount 

        #binary search
        while l <= r: 
            k= (l+r) // 2
            eatingTime= 0
            for p in piles:
                eatingTime += math.ceil(p / k) # calculate eatingTime
            
            #if less than h (max hours), update res and see if there's a smaller eatingSpeed
            if eatingTime <= h:
                res= min(res, k)
                r=k-1
            else: # already above max hours, check smaller half of array
                l=k+1

        return res
