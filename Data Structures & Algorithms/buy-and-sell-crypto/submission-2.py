class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l,r, maxx= 0,1,0

        # [10,1,5,6,7,1]
        # l r

        while r < len(prices): 
            if prices[l] < prices[r]: 
                profit= prices[r] - prices[l]
                maxx= max(maxx, profit)
            else: 
                l = r
            r += 1

        return maxx
        