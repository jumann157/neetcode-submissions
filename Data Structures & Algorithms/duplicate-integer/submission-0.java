class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> set = new HashSet<Integer>();
        boolean hasDuplicate = false;

        for(int i = 0; i < nums.length; i++) {
            int value = nums[i];

            if(!set.contains(value)) {
                set.add(nums[i]);
            } else {
               hasDuplicate = true;
            }
            
        }

        return hasDuplicate;
        
    }
}