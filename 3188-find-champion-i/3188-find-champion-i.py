class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        max_val=float('-inf')
        index=0
        for i in range(0,len(grid)):
            count=0
            for j in range(0,len(grid)):
                if grid[i][j]==1:
                    count+=1
            if count>max_val:
                max_val=count
                index=i
        return index
        
            
        