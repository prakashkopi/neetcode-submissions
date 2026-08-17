class Solution {
    public int maxArea(int[] heights) {
        // find the max height difference by using 2 pointers
        // calculate the max area and update it 

        int left= 0; 
        int right= heights.length -1;

        int res= 0;
        while (left < right) {
            int area= Math.min(heights[left], heights[right]) * (right - left);
            res= Math.max(res, area);

            if (heights[left] <= heights[right]) {
                left += 1;
            }
            else {
                right -= 1;
            }
        }

        return res;

    }
}
