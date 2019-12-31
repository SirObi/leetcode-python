class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        
        valid_pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        
        stack = []
        for bracket in s:
            if bracket in valid_pairs.keys():
                stack.append(bracket)
            elif bracket in valid_pairs.values():
                if stack and bracket == valid_pairs[stack.pop()]:
                    continue
                else:
                    return False
            else:
                print('Not a valid character')
                return False
        return len(stack) == 0
