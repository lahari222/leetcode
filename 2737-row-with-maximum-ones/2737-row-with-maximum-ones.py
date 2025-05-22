class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        new_dict={}
        for i in range(0,len(mat)):
            count=0
            for j in range(0,len(mat[0])):
                if mat[i][j]==1:
                    count+=1
            new_dict[i]=count
        max_val=float('-inf')
        index=0
        for k,v in new_dict.items():
            if v>max_val:
                max_val=max(max_val,v)
                index=k
        return [index,max_val]

        