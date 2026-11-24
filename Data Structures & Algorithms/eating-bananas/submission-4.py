class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def timeTaken(k):
            totalTime= 0
            for p in piles:
                totalTime += math.ceil(p / k)
            return totalTime 
        
        l, r= 1, max(piles)

        res= 0
        while l <= r:
            k= (l+r) // 2
            totalTime= timeTaken(k)
            if totalTime <= h: 
                res= k
                r= k - 1
            else: 
                l= k + 1
        return res
