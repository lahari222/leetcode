class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        #first creating the prefix array
        n=len(nums)
        count=0
        for i in range(1,n):
            nums[i]=nums[i-1]+nums[i]
        for i in range(0,n-1):
            left_sum=nums[i]
            right_sum=nums[n-1]-nums[i]
            if (left_sum-right_sum)%2==0:
                count+=1
        return count
        
        