class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsIndex= {}

        ans= []
        for i, num in enumerate(nums):
            complement= target-num
            if complement in numsIndex:
                ans= [numsIndex[complement], i]
            numsIndex[num]= i
        return ans
        