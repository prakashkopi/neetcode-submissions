class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Three Pointer Approach
            # O(N log N) + O(N^2) time, O(N) space
            # reduces to O(N^2) time, O(N) space

        # Sort array, 
        # if sum > 0 shift left pointer , if sum < 0 shift right pointer
        res= []
        nums.sort()

        for i, a in enumerate(nums):
            # make sure we use a diff index
            if i > 0 and a == nums[i - 1]:
                continue

            # two pointers (basically two sum 2)
            l, r= i + 1, len(nums) - 1
            while l < r: 
                threeSum= a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a,nums[l], nums[r]])
                    l +=1 
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                    
        return res
            




