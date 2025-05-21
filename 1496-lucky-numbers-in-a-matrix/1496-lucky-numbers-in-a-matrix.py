class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        
        row=[]
        col=[]
        for i in range(0,len(matrix)):
            min_val=float('inf')
            for j in range(0,len(matrix[0])):
                if matrix[i][j]<min_val:
                    min_val=matrix[i][j]
            row.append(min_val)
        for i in range(0,len(matrix[0])):
            max_val=float('-inf')
            for j in range(0,len(matrix)):
                if matrix[j][i]>max_val:
                    max_val=matrix[j][i]
            col.append(max_val)
        for i in row:
            if i in col:
                return [i]
        return []


        