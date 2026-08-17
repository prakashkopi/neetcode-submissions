class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r= 0, len(s)-1

        while l < r:
            # skip any c that are not alphanumeric 
            while l < r and not s[l].isalnum(): 
                l +=1
            while r > l and not s[r].isalnum(): 
                r-=1
            if s[l].lower() != s[r].lower(): 
                return False
            # if they are alphanumeric and the same, move pointers towards each other
            l+=1
            r-=1
            
        return True

    # You can also code the function below and call it by doing 
    # self.isAlnum(c) in the above code 
    # def isAlnum(self, c): 
    #     return (ord('A') <= ord(c) <= ord('Z') or 
    #     ord('a') <= ord(c) <= ord('z') or 
    #     ord('0') <= ord(c) <= ord('9'))