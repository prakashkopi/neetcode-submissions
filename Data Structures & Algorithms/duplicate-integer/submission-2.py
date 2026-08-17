class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #hashset to keep track of seen numbers
        seen= set()

        for n in nums: 
            if n in seen: 
                return True
            seen.add(n)
        
        return False

        