class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_val=float('-inf')
        index=0
        for i in range(0,len(mat)):
            count=0
            for j in range(0,len(mat[0])):
                if mat[i][j]==1:
                    count+=1
            if count>max_val:
                max_val=max(max_val,count)
                index=i
        return [index,max_val]

        