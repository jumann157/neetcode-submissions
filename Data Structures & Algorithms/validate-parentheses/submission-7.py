class Solution:
    def isValid(self, s: str) -> bool:
        order = []
        for i in range(0, len(s)):
            if i == 0 and (s[i] == ')' or s[i] == ']' or s[i] == '}'):
                return False
            
            print(order)

            if s[i] == '(':
                order.append('(')
                continue
            elif s[i] == '{':
                order.append('{')
                continue
            elif s[i] == '[':
                order.append('[')
                continue

            # closing brackets
            if s[i] == ')':
                print('-> )')
                if order and order[-1] == '(':
                    del order[-1]
                else:
                    return False
            elif s[i] == ']':
                print('-> ]')
                if order and order[-1] == '[':
                    del order[-1]
                else:
                    return False
            elif s[i] == '}':
                print('-> }')
                if order and order[-1] == '{':
                    del order[-1]
                else:
                    return False
        if not order:
            return True
        else: 
            return False
            



        