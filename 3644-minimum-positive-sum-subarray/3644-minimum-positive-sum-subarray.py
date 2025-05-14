class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        #first find the prefix sum of the array
        min_sum=float('inf')
        n=len(nums)
        sum=0
        for i in range(1,len(nums)):
            nums[i]=nums[i-1]+nums[i]
        #finding the sum of each subarray
        for i in range(l,r+1):
            for j in range(0,n-i+1):
                start=j
                end=j+i-1
                if j==0:
                    sum=nums[end]
                else:
                    sum=nums[end]-nums[start-1]
                if sum>0:
                    min_sum=min(min_sum,sum)
        if min_sum==float('inf'):
            return -1
        else:
            return min_sum