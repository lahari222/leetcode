class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        new_dict={}
        for i in nums:
            if i in new_dict:
                return i
            else:
                new_dict[i]=1
        
                
        