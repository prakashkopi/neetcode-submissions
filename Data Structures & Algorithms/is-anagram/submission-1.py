class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # hashmap to map character -> count 
        # if both hashmaps are equal, return true else false

        sCount, tCount= {}, {}

        # if lengths arent the same, return False by default 
        if len(s) != len(t): 
            return False

        for i in range(len(s)):
            sCount[s[i]]= 1 + sCount.get(s[i], 0)
            tCount[t[i]]= 1 + tCount.get(t[i], 0)

        return sCount == tCount

        
    


        