class MyCircularQueue:

    def __init__(self, k: int):
        self.k=k
        self.circular_queue=[]
        

    def enQueue(self, value: int) -> bool:
        if len(self.circular_queue)==self.k:
            return False
        else:
            self.circular_queue.append(value)
            return True
        

    def deQueue(self) -> bool:
        if len(self.circular_queue)>0:
            pop_ele=self.circular_queue.pop(0)
            return True
        else:
            return False
        

    def Front(self) -> int:
        if len(self.circular_queue)>0:
            return self.circular_queue[0]
        else:
            return -1
        

    def Rear(self) -> int:
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
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()