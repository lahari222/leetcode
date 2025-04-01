class FrontMiddleBackQueue:

    def __init__(self):
        self.new_queue=[]
        

    def pushFront(self, val: int) -> None:
        if len(self.new_queue)==0:
            self.new_queue.append(val)
        else:
            self.new_queue.insert(0,val)
        

    def pushMiddle(self, val: int) -> None:
        middle=len(self.new_queue)//2
        self.new_queue.insert(middle,val)
        

    def pushBack(self, val: int) -> None:
        self.new_queue.append(val)
        

    def popFront(self) -> int:
        
        if len(self.new_queue)>0:
            pop_ele=self.new_queue.pop(0)
            return pop_ele
        else:
            return -1
    def popMiddle(self) -> int:
        if len(self.new_queue)>0:
            if len(self.new_queue)%2==0:
                middle=len(self.new_queue)//2
                pop_ele=self.new_queue.pop(middle-1)
                return pop_ele
            else:
                middle=len(self.new_queue)//2
                pop_ele=self.new_queue.pop(middle)
                return pop_ele
        else:
            return -1
    def popBack(self) -> int:
        if len(self.new_queue)>0:
            pop_ele=self.new_queue.pop()
            return pop_ele
        else:
            return -1
        


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()