class Solution:
    def isValid(self, s: str) -> bool:
        stack  = []
        for char in s:
            if char in ['(', '[', '{']:
                stack.append(char)
                print(stack)
            else:
                if not stack:
                    return False
                char_pop = stack.pop()
                print(char_pop)
                if char_pop == '(' and char != ')' or char_pop == '[' and char != ']' or char_pop == '{' and char != '}':
                    return False
        return False if stack else True
