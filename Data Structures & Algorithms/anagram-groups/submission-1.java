class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> output = new ArrayList<>();
        HashMap<String, List<String>> map = new HashMap<>();

        for(String word : strs) { // act 1010000000100
            int[] count = new int[26]; // space for each letter

            for(Character c : word.toCharArray()) {
                count[c - 'a'] += 1; // 'a' - 'a' = 0, 'z' - 'a' = 26
            }

            String string = Arrays.toString(count);

            if(!map.keySet().contains(string)) {
               map.put(string, new ArrayList<String>());
            }
            List<String> subL = map.get(string);
            subL.add(word);
            map.put(string, subL);
            
        }

        for(List<String> sublist : map.values()) {
            output.add(sublist);
        }
            
        return output;
        
    }
}
