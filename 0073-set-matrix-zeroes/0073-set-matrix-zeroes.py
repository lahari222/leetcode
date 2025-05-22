class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_zero=set()
        col_zero=set()
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                if matrix[i][j]==0:
                    row_zero.add(i)
                    col_zero.add(j)
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                if i in row_zero and matrix[i][j]!=0:
                    matrix[i][j]=0
        for i in range(0,len(matrix[0])):
            for j in range(0,len(matrix)):
                if i in col_zero and matrix[j][i]!=0:
                    matrix[j][i]=0
        return matrix
        
        