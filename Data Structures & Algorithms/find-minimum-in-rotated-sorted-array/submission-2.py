class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r= 0, len(nums)-1
        res= nums[0] # default to any value

        while l <= r:
            # if array is already sorted
            if nums[l] < nums[r]:
                res= min(res, nums[l])
                break
            
            # if array is rotated, perform the binary search
            m= (l+r) // 2
            res= min(res, nums[m])
            
            if nums[m] >= nums[l]:
                l= m + 1
            else:
                r= m - 1

        return res
            

    
    
        