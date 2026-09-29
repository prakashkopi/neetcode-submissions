class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # recursive backtracking
        res= []

        def backtrack(i, currentCombo, total): 
            # base case, if total == target, we add copy to res and return
            if total == target: 
                res.append(currentCombo[:])
            
            # base case, if we go over or reach end of candidates 
            # (nums) array, stop going down that path 
            if i == len(nums) or total >= target: 
                return 
            
            # choose
            currentCand= nums[i]
            currentCombo.append(currentCand)
            backtrack(i, currentCombo, total + currentCand)
            
            # undo/backtrack
            currentCombo.pop()
            backtrack(i+1, currentCombo, total)

        backtrack(0, [], 0)
        return res
        