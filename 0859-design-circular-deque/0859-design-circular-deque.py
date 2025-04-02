class MyCircularDeque:

    def __init__(self, k: int):
        self.k=k
        self.circular_queue=[]
        

    def insertFront(self, value: int) -> bool:
        if len(self.circular_queue)==self.k:
            return False
        else:
            self.circular_queue.insert(0,value)
            return True
        

    def insertLast(self, value: int) -> bool:
        if len(self.circular_queue)==self.k:
            return False
        else:
            self.circular_queue.append(value)
            return True
        

    def deleteFront(self) -> bool:
        if len(self.circular_queue)>0:
            pop_ele=self.circular_queue.pop(0)
            return True
        else:
            return False
        

    def deleteLast(self) -> bool:
        if len(self.circular_queue)>0:
            pop_ele=self.circular_queue.pop()
            return True
        else:
            return False
        

    def getFront(self) -> int:
        if len(self.circular_queue)>0:
            return self.circular_queue[0]
        else:
            return -1
        

    def getRear(self) -> int:
        if len(self.circular_queue)>0:
            return self.circular_queue[-1]
        else:
            return -1
        

    def isEmpty(self) -> bool:
        if len(self.circular_queue)==0:
            return True
        else:
            return False
        

    def isFull(self) -> bool:
        if len(self.circular_queue)==self.k:
            return True
        else:
            return False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()