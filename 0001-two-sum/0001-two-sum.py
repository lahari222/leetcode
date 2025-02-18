class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary={}
        for i in range(0,len(nums)):
            result=target-nums[i]
            if result in dictionary:
                return [i,dictionary[result]]
            else:
                dictionary[nums[i]]=i
        return new_list
        