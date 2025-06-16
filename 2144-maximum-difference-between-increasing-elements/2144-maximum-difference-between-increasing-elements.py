class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_ele=float('-inf')
        max_diff=float('-inf')
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j]>nums[i] and abs(nums[j]-nums[i])>max_diff:
                    max_diff=max(max_diff,abs(nums[j]-nums[i]))
        if max_diff==float('-inf'):
            return -1
        else:
            return max_diff
        