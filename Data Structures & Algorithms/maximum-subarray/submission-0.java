class Solution {
    public int maxSubArray(int[] nums) {
        // -2 1 3 4 -1 2 1 -5 4
        //    l r
        int left = 0;
        int right = 1;
        int prefix = nums[left];
        int max = prefix;

        while(right < nums.length) {
            System.out.println("left: " + left);
            System.out.println("right: " + right);
            System.out.println("prefix: " + prefix);
            System.out.println("max: " + max);
            prefix += nums[right];
            if(prefix < nums[right]) {
                left = right;
                prefix = nums[right];
            }

            if(prefix > max) {
                max = prefix;
            }
            right++;
        }
        return max;
    }
}
