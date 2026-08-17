class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap num : index
        # difference = target-num
        # difference is the key so return the value of that key to get index
        mpp= {}

        for i, n in enumerate(nums):
            difference= target - n
            if difference in mpp:
                return [mpp[difference], i]
            mpp[n]= i #if difference isnt found, add num and index to hashmap
        



        