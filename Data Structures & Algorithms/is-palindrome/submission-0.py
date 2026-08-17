class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Interviewer might not want you to use isalnum and implement it yourself instead
        # Interviewer might not want you to use extra memory
        
        newStr= ""

        for c in s:
            if c.isalnum():
                newStr+= c.lower()
        
        return newStr == newStr[::-1]

        