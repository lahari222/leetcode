class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum,ans=0,0
        n=len(nums)
        max_sum=float('-inf')
        for i in range(0,k):
            current_sum+=nums[i]
        ans=current_sum/k
        max_sum=max(max_sum,ans)
        for i in range(1,n-k+1):
            start=i
            end=start+k-1
            current_sum=current_sum-nums[start-1]+nums[end]
            ans=current_sum/k
            max_sum=max(max_sum,ans)
        return max_sum