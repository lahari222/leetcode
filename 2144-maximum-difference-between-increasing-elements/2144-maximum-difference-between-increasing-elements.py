class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_diff=-1
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j]>nums[i] and abs(nums[j]-nums[i])>max_diff:
                    max_diff=max(max_diff,abs(nums[j]-nums[i]))
        return max_diff        