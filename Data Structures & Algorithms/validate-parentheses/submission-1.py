class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        closeToOpen = { ")" : "(", 
                        "]" : "[", 
                        "}" : "{"}
                        # key : closing parenthesis
                        # val : opening parenthesis that needs to match

        for c in s:
            if c in closeToOpen:    
                if stack and stack[-1] == closeToOpen[c]:
                    # stack[-1] = most recent opening bracket
                    # closeToOpen[c] = required opening bracket
                    # If they match → valid pair → remove it
                    stack.pop() 
                else: 
                    return False
            else:
                stack.append(c)

        if not stack: # if the stack is empty then it means all parentheses were matched
            return True
        
        return False