class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the input array
        # check the prev value and if it's the same, skip it
        res= []
        nums.sort()

        for i, a in enumerate(nums): 
            # we dont want to use the same value in same position twice
            # so we check if the prev index value is the same and if it is, skip it
            if i > 0 and a == nums[i-1]: 
                continue

            l, r= i+1, len(nums) -1
            while l < r: 
                threeSum= a + nums[l] + nums[r]

                if threeSum > 0: 
                    r -=1 
                elif threeSum < 0: 
                    l += 1
                else: 
                    res.append([a, nums[l], nums[r]])
                    r -=1
                    while nums[r] == nums[r+1] and r > l: 
                        r-= 1
        return res
                     

            

         
        