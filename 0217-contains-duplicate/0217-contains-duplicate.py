class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        new_dict={}
        for i in nums:
            if i in new_dict:
                new_dict[i]+=1
            else:
                new_dict[i]=1
        for k,v in new_dict.items():
            if v>1:
                return True
        return False
        