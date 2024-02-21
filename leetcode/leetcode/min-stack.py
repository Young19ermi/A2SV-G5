class MinStack:

    def __init__(self):
        self.minstack = []
        self.object = [] 

    def push(self, val: int) -> None:
        self.object.append(val)
        if not self.minstack or val <= self.minstack[-1]:
            self.minstack.append(val)
        

    def pop(self) -> None:
        if not self.object:
            return -1 
        if self.object[-1] == self.minstack[-1]:    
            self.minstack.pop()       
        return self.object.pop()    
        

    def top(self) -> int:
        if not self.object:
            return 0
        return self.object[-1]
        

    def getMin(self) -> int:
        if not self.minstack:
            return None
        return self.minstack[-1]


        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()