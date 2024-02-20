from collections import deque
class MyStack:

    def __init__(self):
        self.list = deque()
        

    def push(self, x: int) -> None:
        self.list.append(x)
        

    def pop(self) -> int:
        if not self.list:
            return None
        return self.list.pop()    
        

    def top(self) -> int:
        if not self.list:
            return -1
        return self.list[-1]
    def empty(self) -> bool:
        if len(self.list) == 0:
            return True
        return False                


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()