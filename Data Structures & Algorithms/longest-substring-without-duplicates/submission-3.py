class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_set = set([])
        a, b = 0, 0
        max_len = 0

        while b < len(s):
            letter = s[b]
            # if letter if already in set (duplicate found)
            if letter in unique_set:
                max_len = max(max_len, len(unique_set)) # get max
                # remove all letters up until the first occurence of duplicate letter
                while s[a] != s[b]:
                    unique_set.remove(s[a])
                    a += 1
                if s[a] == s[b]:
                    unique_set.remove(s[a])
                    a += 1
            unique_set.add(letter) # add letter to set and increment
            b += 1
        return max(max_len, len(unique_set))