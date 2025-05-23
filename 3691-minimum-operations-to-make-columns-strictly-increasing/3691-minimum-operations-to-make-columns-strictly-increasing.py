class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        total_sum=0
        for i in range(0,len(grid[0])):
            for j in range(1,len(grid)):
                if grid[j][i]<=grid[j-1][i]:
                    curr=(grid[j-1][i]-grid[j][i])+1
                    grid[j][i]=grid[j][i]+curr
                    total_sum+=curr
        return total_sum
                    
        