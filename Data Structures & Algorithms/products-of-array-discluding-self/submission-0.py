class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
    
        # Initialize the output array with 1s
        answer = [1] * n
        
        # Calculate the prefix product for each element
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
        
        # Calculate the postfix product for each element and multiply with the prefix product
        postfix = 1
        for i in range(n-1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]
        
        return answer