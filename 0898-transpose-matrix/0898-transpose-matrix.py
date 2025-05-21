class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result=[]
        for i in range(0,len(matrix[0])):
            new=[]
            for j in range(0,len(matrix)):
                new.append(matrix[j][i])
            result.append(new)
        return result