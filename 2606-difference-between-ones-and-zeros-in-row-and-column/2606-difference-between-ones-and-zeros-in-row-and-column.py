class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        result=[]
        row_one=[]
        row_zero=[]
        col_one=[]
        col_zero=[]
        total=0
        for i in range(0,len(grid)):
            row_count_one,row_count_zero=0,0
            for j in range(0,len(grid[0])):
                if grid[i][j]==1:
                    row_count_one+=1
                else:
                    row_count_zero+=1
            row_one.append(row_count_one)
            row_zero.append(row_count_zero)
        for i in range(0,len(grid[0])):
            col_count_one,col_count_zero=0,0
            for j in range(0,len(grid)):
                if grid[j][i]==1:
                    col_count_one+=1
                else:
                    col_count_zero+=1
            col_one.append(col_count_one)
            col_zero.append(col_count_zero)
        for i in range(0,len(row_one)):
            diff=[]
            for j in range(0,len(col_one)):
                total=row_one[i]+col_one[j]-row_zero[i]-col_zero[j]
                diff.append(total)
            result.append(diff)
        return result
            



        