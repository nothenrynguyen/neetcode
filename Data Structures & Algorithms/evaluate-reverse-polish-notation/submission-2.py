class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        # 5 cases:
        # 1 - digit
        # or any of the 4 operations

        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))    # we use int here cuz in python this converts to int and rounds towards 0
            else:                           # or it's a number
                stack.append(int(c))        # we convert to int cuz it's originally given as a character

        return stack[0]

        # + and * are easy cuz order doesn't matter
        # but - and / are slightly more complicated cuz it's still left-to-right order

        # this is time O(n) cuz we iterate thru the array once 
        # and also space O(n) cuz we create one array/stack