class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        initial=0
        for i in range(0,len(nums)):
            if nums[i]%2==0:
                nums[initial],nums[i]=nums[i],nums[initial]
                initial+=1
        return nums