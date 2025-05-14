class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        sum=0
        prefix_array=[0]*len(nums)
        prefix_array[0]=nums[0]
        #finding prefix sum array
        for i in range(1,len(nums)):
            prefix_array[i]=prefix_array[i-1]+nums[i]
        for i in range(0,len(nums)):
            start=max(0,i-nums[i])
            if start==0:
                sum+=prefix_array[i]
            else:
                sum+=prefix_array[i]-prefix_array[start-1]
        return sum

        
        
        