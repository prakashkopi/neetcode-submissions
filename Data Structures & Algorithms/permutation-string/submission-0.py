class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2= len(s1), len(s2)

        if n1 > n2: 
            return False
        
        s1Count= [0] * 26
        s2Count= [0] * 26

        # go through first string and count frequencies of each char
        for i in range(n1): 
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        # if we found a permutation after going through s1, return true
        if s1Count == s2Count: 
            return True 
        
        # sliding window starting from end of s1 until end of s2
        for i in range(n1, n2): 
            s2Count[ord(s2[i]) - ord('a')] += 1
            s2Count[ord(s2[i-n1]) - ord('a')] -= 1
            # if counts match, return True 
            if s1Count == s2Count: 
                return True 
        
        # never found a valid perm, return False
        return False

