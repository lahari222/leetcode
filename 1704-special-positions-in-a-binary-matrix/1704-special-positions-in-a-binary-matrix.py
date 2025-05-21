class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row_one,col_one=[],[]
        count=0
        for i in range(0,len(mat)):
            row_count=0
            for j in range(0,len(mat[0])):
                if mat[i][j]==1:
                    row_count+=1
            row_one.append(row_count)
        for i in range(0,len(mat[0])):
            col_count=0
            for j in range(0,len(mat)):
                if mat[j][i]==1:
                    col_count+=1
            col_one.append(col_count)
        for i in range(0,len(mat)):
            for j in range(0,len(mat[0])):
                if mat[i][j]==1:
                    if row_one[i]==1 and col_one[j]==1:
                        count+=1
        return count

        