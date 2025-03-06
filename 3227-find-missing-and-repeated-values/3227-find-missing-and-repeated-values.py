class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        result=0
        n=len(grid)
        m=len(grid[0])
        new_list=[0]*(n*n)
        for i in range(0,n):
            for j in range(0,m):
                new_number=grid[i][j]
                if new_number in new_list:
                    result=new_number
                else:
                    new_list[new_number-1]=new_number
        for i in range(0,len(new_list)):
            if new_list[i]==0:
                return [result,i+1]
        
        