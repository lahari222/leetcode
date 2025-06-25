class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        max_one,max_zero=0,0
        cur_one,cur_zero=0,0
        for i in s:
            if i=='1':
                cur_zero=0
                cur_one+=1
            else:
                cur_zero+=1
                cur_one=0
            max_one=max(max_one,cur_one)
            max_zero=max(max_zero,cur_zero) 
        return max_one>max_zero  