class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        result=[]
        new_result=[]
        for j in range(0,len(mat[0])):
            i=0
            mini_result=[]
            while i<len(mat) and j>=0:
                mini_result.append(mat[i][j])
                i+=1
                j-=1
            result.append(mini_result)
        for i in range(1,len(mat)):
            j=len(mat[0])-1
            mini_result=[]
            while i<len(mat) and j>=0:
                mini_result.append(mat[i][j])
                i+=1
                j-=1
            result.append(mini_result)
        for i in range(0,len(result)):
            if i%2==0:
                k=0
                j=len(result[i])-1
                while k<j:
                    result[i][k],result[i][j]=result[i][j],result[i][k]
                    k+=1
                    j-=1        
        for i in range(0,len(result)):
            for j in range(0,len(result[i])):
                new_result.append(result[i][j])
        return new_result
        