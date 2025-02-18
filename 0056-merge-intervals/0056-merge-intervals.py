class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        new_list=[]
        current_start=intervals[0][0]
        current_end=intervals[0][1]
        next_start=0
        next_end=0
        for i in range(1,len(intervals)):
            next_start=intervals[i][0]
            next_end=intervals[i][1]
            if current_end<next_start:
                new_list.append([current_start,current_end])
                current_start=next_start
                current_end=next_end
            else:
                current_start=min(current_start,next_start)
                current_end=max(current_end,next_end)
        new_list.append([current_start,current_end])
        return new_list
            
        