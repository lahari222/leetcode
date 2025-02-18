class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        new_dict={}
        for i in nums:
            if i in new_dict:
                return True
            new_dict[i]=1
        return False
            
        