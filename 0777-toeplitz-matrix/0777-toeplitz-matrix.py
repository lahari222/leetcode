class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        new_list=[]
        for j in range(0,len(matrix[0])):
            i=0
            mini_list=set()
            while i<len(matrix) and j<len(matrix[0]):
                mini_list.add(matrix[i][j])
                i+=1
                j+=1
            new_list.append(mini_list)
        for i in range(1,len(matrix)):
            j=0
            mini_list=set()
            while i<len(matrix) and j<len(matrix[0]):
                mini_list.add(matrix[i][j])
                i+=1
                j+=1
            new_list.append(mini_list)
        for i in range(0,len(new_list)):
            if len(new_list[i])>1:
                return False
        return True
        