class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum=0
        i=0
        max_sum=float('-inf')
        while i<len(nums):
            current_sum+=nums[i]
            if current_sum<0:
                current_sum=0
            max_sum=max(max_sum,current_sum)
            i+=1
        if max_sum==0:
            return max(nums)
        else:
            return max_sum
            

        