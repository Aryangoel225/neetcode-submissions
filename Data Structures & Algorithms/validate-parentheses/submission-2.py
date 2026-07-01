class Solution:
    def isValid(self, s: str) -> bool:
        # stack 
        stack = []
        # create a hashmap
        sets = {"(": ")", "[": "]", "{": "}"}
        # check each char in str
        for char in s:
            # check if in keys (open bracket)
            if char in sets:
                stack.append(char) # if so add to stack
            else: # closing bracket
                if stack:
                    o = stack.pop()
                    if sets[o] != char: # if openbracket key's value doesn't match char return false
                        return False
                else:
                    return False

        return len(stack) == 0 # return if empty stack after loop