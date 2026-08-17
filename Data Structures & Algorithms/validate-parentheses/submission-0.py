class Solution:
    def isValid(self, s: str) -> bool:
        # Stack Approach with a hashmap
        # O(N) time and space
        stack= []
        closeToOpen={')' : '(', ']' : '[', '}': '{'}

        # have to start with open paranthesis
        # once there's an open and close, we can remove them

        for c in s: 
            # check if closing paranthesis
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                # if paranthesis don't match or stack is empty, return False
                else:
                    return False
            else:
                stack.append(c)
        
        # Only return true if stack is empty
        return True if not stack else False

        
                

        




        