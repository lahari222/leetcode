class Solution:
    def isValid(self, s: str) -> bool:
        new_list = []
        for char in s:
            if char in "({[":
                new_list.append(char)
            elif char in ")}]":
                if not new_list:
                    return False
                if (char == ')' and new_list[-1] == '(') or (char == ']' and new_list[-1] == '[') or (char == '}' and new_list[-1] == '{'):
                    new_list.pop()
                else:
                    return False
        
        return len(new_list) == 0
        
        