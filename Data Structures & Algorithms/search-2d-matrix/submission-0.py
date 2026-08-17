class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Call binary search on first column to determine which row the value is in
        # Use binary search again in the specific row to find the target
        # O(log(m*n)) time, O(1) space

        if not matrix or not matrix[0]:
            return False

        rows, cols = len(matrix), len(matrix[0])
        top, bot= 0, rows -1

        # Binary search to find current row
        while top <= bot:
            row= (top + bot) // 2
            if target > matrix[row][-1]:
                top= row + 1
            elif target < matrix[row][0]:
                bot= row - 1
            else:
                break

        # Check if row is valid
        if not top <= bot:
            return False
        
        row = (top + bot) // 2

        # Call binary search function on the specified row
        return self.binarySearch(matrix[row], target)

    def binarySearch(self, nums, target):
        l, r= 0, len(nums) - 1

        while l <= r:
            m= (l+r) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return True

        return False

    


        