class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        closeToOpen = { ")" : "(", "]" : "[", "}" : "{"}

        for c in s:
            if c in closeToOpen:    # checks if the char is a closing parenthesis cuz the keys in our map are closing
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(c)

        if not stack: # if the stack is empty
            return True
        
        return False