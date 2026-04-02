class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:                       # if the minStack is not empty
            val = min(val, self.minStack[-1])   # we keep minimum of the val and the current top of minStack
        self.minStack.append(val)               # else we just keep the val cuz its the min
    
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
