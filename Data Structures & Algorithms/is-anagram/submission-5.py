class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = {} # letter : count
        t_dict = {}

        for letter in s:
            if letter in s_dict:
                s_dict[letter] = s_dict[letter] + 1
            else:
                s_dict[letter] = 1
        
        for letter in t:
            if letter in t_dict:
                t_dict[letter] = t_dict[letter] + 1
            else:
                t_dict[letter] = 1
        
        return s_dict == t_dict
        