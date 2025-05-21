class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n=len(matrix)
        for i in range(n):
            row=set()
            col=set()
            for j in range(n):
                row.add(matrix[i][j])
                col.add(matrix[j][i])
            if len(row)!=n or len(col)!=n:
                return False
        return True