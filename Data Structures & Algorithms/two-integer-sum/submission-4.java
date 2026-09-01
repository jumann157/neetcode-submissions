class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] result = new int[2];

        ArrayList<Integer> list = new ArrayList<>();

        for(int n : nums) {
            list.add(Integer.valueOf(n));
        }

        for(int i = 0; i < list.size(); i++) {
            int t = target - nums[i];
            System.out.println("target: " + t);
            
            if(list.contains(t)) {
                result[0] = i;

                int possible = list.lastIndexOf(t);
                if(possible == i) {
                    continue;
                } else {
                    result[1] = possible;
                }
                System.out.println(result[0] + " " + result[1]);
                break;
            }
        }
        return result;
    }
}
