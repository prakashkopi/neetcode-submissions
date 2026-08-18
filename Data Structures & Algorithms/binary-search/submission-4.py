class Solution:
    def search(self, nums: List[int], target: int) -> int:


        return self.binarySearch(nums, target)

    def binarySearch(self, nums, target): 
        l, r= 0, len(nums) -1

        while l <= r: 
            m= (l + r) // 2 # can lead to overflow
            # m= l + ((r-l) // 2)
            if nums[m] < target: 
                l= m+1
            elif nums[m] > target: 
                r= m-1
            else: 
                return m
        
        return -1
    
        