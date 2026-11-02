class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeBracketMap = {
            ')':'(', 
            '}':'{',
            ']':'['
        }

        for c in s:
            if c in closeBracketMap:
                if stack and stack[-1] == closeBracketMap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False

           