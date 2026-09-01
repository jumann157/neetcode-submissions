class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()) {
            return false;
        }

        HashMap<Character, Integer> mapS = new HashMap<Character, Integer>();
        HashMap<Character, Integer> mapT = new HashMap<Character, Integer>();
        for(int i = 0; i < s.length(); i++) {
            if(mapS.containsKey(s.charAt(i))) {
                char keyS = s.charAt(i);
                mapS.put(keyS, mapS.get(keyS) + 1);
            } else {
                mapS.put(s.charAt(i), 0);
            }

            if(mapT.containsKey(t.charAt(i))) {
                char keyT = t.charAt(i);
                int update = mapT.get(keyT) + 1;
                mapT.put(keyT, update);
            } else {
                mapT.put(t.charAt(i), 0);
            }
        }

        if(mapS.equals(mapT)){
            return true;
        }

        return false;
    }
}
