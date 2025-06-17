class MyCalendar:

    def __init__(self):
        self.new_list=[]
        

    def book(self, startTime: int, endTime: int) -> bool:
        for i in self.new_list:
            if (startTime<i[0] and endTime>i[0]) or startTime==i[0] or (startTime>i[0] and startTime<i[1]):
                return False
        self.new_list.append([startTime,endTime])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)