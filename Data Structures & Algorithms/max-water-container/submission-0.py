class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Two Pointer Approach
            # O(N) time, O(1) space

        # left at beginning, right at end
        # keep track of the max area between the two pointers
        # shift the pointer with the lower height

        res= 0
        l, r= 0, len(heights) -1

        while l < r:
            area= (r-l) * min(heights[l], heights[r])
            res= max(res, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r-= 1
        return res

        