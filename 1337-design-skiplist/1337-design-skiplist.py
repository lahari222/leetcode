class Skiplist:

    def __init__(self):
        self.linked_list=[]
        

    def search(self, target: int) -> bool:
        if target in self.linked_list:
            return True
        else:
            return False
        

    def add(self, num: int) -> None:
        self.linked_list.append(num)
        

    def erase(self, num: int) -> bool:
        if num in self.linked_list:
            self.linked_list.remove(num)
            return True
        else:
            return False



# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)