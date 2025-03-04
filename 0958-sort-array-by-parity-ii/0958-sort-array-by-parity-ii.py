class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd=1
        even=0
        while odd<len(nums) and even<len(nums):
            if nums[even]%2==0:
                even+=2
            elif nums[odd]%2!=0:
                odd+=2
            else:
                nums[even],nums[odd]=nums[odd],nums[even]
                even+=2
                odd+=2
        return nums
       