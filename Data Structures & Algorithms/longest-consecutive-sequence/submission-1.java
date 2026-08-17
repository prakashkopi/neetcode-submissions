class Solution {
    public int longestConsecutive(int[] nums) {

        // Create a set of the array so we can check against it 
        Set<Integer> numSet= new HashSet<>();
        for (int num: nums) {
            numSet.add(num);
        }
        int longest= 0;

        for (int num: numSet) {
            // Check if start of a sequence
            if (!numSet.contains(num-1)) {
                int length= 1;
                while (numSet.contains(num + length)) {
                    length++;
                }
                // update longest with the max
                longest= Math.max(longest, length);
            }
        }

        return longest;
        
    }
}
