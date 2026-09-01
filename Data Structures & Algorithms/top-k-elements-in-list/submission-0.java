class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // holds the count of each element in nums
        HashMap<Integer, Integer> map = new HashMap<Integer,Integer>();
        // multi-indexed array, places the freq of each element in the corresponding index
        List<Integer>[] freq = new List[nums.length + 1]; 

        for(int i = 0; i < freq.length; i++) {
            freq[i] = new ArrayList<>();
        }
        
        // counts the freq and adds to map
        for(int n : nums) {
            map.putIfAbsent(n, 0);
            map.put(n, map.get(n) + 1);
        }

        // add to freq
        for(Map.Entry<Integer, Integer> entry : map.entrySet()) {
            freq[entry.getValue()].add(entry.getKey());
        }

        // traverse freq to find top k
        int[] res = new int[k];
        int index = 0;
        
        for(int i = freq.length - 1; i > 0 && index < k; i--) {
            if(freq[i] != null) {
                for(int n : freq[i]) {
                    res[index] = n;
                    index++;

                    if(k == index) {
                        return res;
                    }
                }
            }
        }

        return res;
        

   }
}
