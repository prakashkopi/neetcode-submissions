class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit= 0
        lowest= prices[0]
        for p in prices:
            if p < lowest:
                lowest= p
            profit= max(profit, p - lowest)
        return profit

        