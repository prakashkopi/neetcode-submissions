class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, maxx= 0,0
        unique= set() 

        for r in range(len(s)): 
            # if char in set, remove and shrink window
            while s[r] in unique: 
                unique.remove(s[l])
                l+=1
            unique.add(s[r])
            maxx= max(maxx, r-l+1)
        return maxx