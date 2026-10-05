class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # similar to combination sum but sort array and skip dups
        candidates.sort()
        res= []

        def backtrack(i, currentCombo, total):
            if total == target: 
                res.append(currentCombo[:])
                return

            # base case - we reach end of candidates array
            # or total > target
            if i == len(candidates) or total > target: 
                return

            currentCand= candidates[i]
            currentCombo.append(currentCand)
            backtrack(i+1, currentCombo, total + currentCand)

            # skip dups 
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]: 
                i += 1

            # undo/backtrack
            currentCombo.pop()
            backtrack(i+1, currentCombo, total)

        backtrack(0, [], 0)
        return res