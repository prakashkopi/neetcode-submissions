class MinStack:

    def __init__(self):
        self.stack= []
        self.minStack= []
        

    def push(self, val: int) -> None:
        self.stack.append(val) # adds new val to top of stack
        val= min(val, self.minStack[-1] if self.minStack else val) # gets minimum value.
        self.minStack.append(val)

    def pop(self) -> None:
        # pop off top (last) element
        # self.minStack.remove(self.stack[-1]) # remove value from the minStack as well 
        # self.stack= self.stack[:-1]

        # can also do this as it's easier        
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1] # gets top element 
        

    def getMin(self) -> int:
        return self.minStack[-1]
        
