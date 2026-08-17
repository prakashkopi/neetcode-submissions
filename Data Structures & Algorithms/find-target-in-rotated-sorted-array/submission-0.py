class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r= 0, len(nums)-1

        while l <= r:
            m= (l+r) // 2
            if nums[m] == target:
                return m
            
            # Determine which half is sorted
            if nums[l] <= nums[m]: # left portion is sorted
                if nums[l] <= target < nums[m]:
                    return self.binarySearch(nums,l,r,target)
                l= m+1
            else: # Right portion is sorted
                if nums[m] < target <= nums[r]:
                    return self.binarySearch(nums,l,r,target)
                r= m-1
            
        return -1

    # Binary search helper function
    def binarySearch(self, nums, l, r, target): 
        while l <= r:
            m= (l+r) // 2

            if target > nums[m]:
                l= m+1
            elif target < nums[m]:
                r= m-1
            else:
                return m
        return -1
            
