class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        int diff = 0;
        int[] indices = new int[2];
        for(int i = 0; i < nums.length; i++) {
            diff = target - nums[i];
            if(map.get(diff) != null) {
                indices[0] = map.get(diff);
                indices[1] = i;
                break;
            }

            map.put(nums[i], i);
        }
        return indices;
    }
}
