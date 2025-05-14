class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        result_array=[]
        max_ele=nums[0]
        for i in range(0,len(nums)):
            if nums[i]>max_ele:
                max_ele=nums[i]
            result=nums[i]+max_ele
            result_array.append(result)
        for i in range(1,len(result_array)):
            result_array[i]=result_array[i-1]+result_array[i]
        return result_array
