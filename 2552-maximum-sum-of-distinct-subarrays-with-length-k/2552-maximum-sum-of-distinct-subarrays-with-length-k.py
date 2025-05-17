class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        window_sum,max_val=0,0
        new_dict={}
        for i in range(0,k):
            if nums[i] not in new_dict:
                new_dict[nums[i]]=1
            else:
                new_dict[nums[i]]+=1
            window_sum+=nums[i]
        if len(new_dict)==k:
            max_val=max(max_val,window_sum)
        for i in range(1,n-k+1):
            start=i
            end=start+k-1
            window_sum=window_sum+nums[end]-nums[start-1]
            if nums[end] in new_dict:
                new_dict[nums[end]]+=1
            else:
                new_dict[nums[end]]=1
            if nums[start-1] in new_dict and new_dict[nums[start-1]]==1:
                del new_dict[nums[start-1]]
            if nums[start-1] in new_dict and new_dict[nums[start-1]]>1:
                new_dict[nums[start-1]]-=1
            if len(new_dict)==k:
                max_val=max(max_val,window_sum)
        return max_val