class MinStack:

    def __init__(self):
        self.new_arr=[]
        

    def push(self, val: int) -> None:
        self.new_arr.append(val)
        

    def pop(self) -> None:
        if len(self.new_arr)>0:
            self.new_arr.pop()

        

    def top(self) -> int:
        return self.new_arr[-1]
        
        

    def getMin(self) -> int:
        return min(self.new_arr)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()