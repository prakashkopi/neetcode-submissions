class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count= {}
        l, freq= 0,0

        for r in range(len(s)): 
            count[s[r]]= count.get(s[r], 0) + 1
            freq= max(freq, count[s[r]])

            window= r-l+1
            if window - freq > k: 
                count[s[l]] -=1
                l +=1
            finalWindow= r-l+1 #recalculate to update stale window
        return finalWindow
        