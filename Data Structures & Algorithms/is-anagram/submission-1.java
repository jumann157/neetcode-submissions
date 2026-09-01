class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()) {
            return false;
        }

        // create hashmap to map all letters and the num of occurences
        HashMap<Character, Integer> map = new HashMap<>();
        for(char letterS : s.toCharArray()) {
            if(map.computeIfPresent(letterS, (letter, count) -> count + 1) == null) {
                map.put(letterS, 1);
            }
        }


        for(char letterT : t.toCharArray()) {
            // if letter doesnt exist in map, return false
            if(!map.containsKey(letterT)) {
                return false;
            }
            // else, check if count goes below 0
            int value = map.compute(letterT, (letter, count) -> count - 1);

            if(value < 0) {
                return false;
            }
        }

        return true;
    }
}
