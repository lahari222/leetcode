class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        new_dict={}
        for i in range(0,len(matrix[0])):
            max_ele=float('-inf')
            for j in range(0,len(matrix)):
                if matrix[j][i]>max_ele:
                    max_ele=max(max_ele,matrix[j][i])
            new_dict[i]=max_ele
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                if matrix[i][j]==-1:
                    matrix[i][j]=new_dict[j]
        return matrix
        

        