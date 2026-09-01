class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_s = s.lower()
        l, r = 0, len(s) - 1
        # no lemon, no melon
        #  l              r
        print(lower_s)
        while r > l:
            while l < len(s) and not lower_s[l].isalnum():
                l += 1
            while r >= 0 and not lower_s[r].isalnum():
                r -= 1
            if l >= r:
                break
            if lower_s[l] != lower_s[r]:
                return False
            l += 1
            r -= 1
        return True
        