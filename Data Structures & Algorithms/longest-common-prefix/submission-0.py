class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # vert scan
        firstWord= strs[0]
        for i in range(len(firstWord)): 
            for s in strs: 
                # if i gets to end of current string or we find mismatch
                # return the value up to s[i] as that's our answer
                if i == len(s) or s[i] != firstWord[i]: 
                    return s[:i]
        return firstWord