import random
class RandomizedCollection:

    def __init__(self):
        self.nums=[]
        

    def insert(self, val: int) -> bool:
        if val in self.nums:
            self.nums.append(val)
            return False
        else:
            self.nums.append(val)
            return True
        

    def remove(self, val: int) -> bool:
        if val in self.nums:
            self.nums.remove(val)
            return True
        else:
            return False

        

    def getRandom(self) -> int:
        return random.choice(self.nums)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()