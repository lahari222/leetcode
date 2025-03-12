class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        new_dict={}
        cal_sum=0
        max_sum=0
        for i in range(0,k):
            if nums[i] in new_dict:
                new_dict[nums[i]]+=1
            else:
                new_dict[nums[i]]=1
            cal_sum+=nums[i]
        if len(new_dict)>=m:
            max_sum=max(max_sum,cal_sum)
        for i in range(1,len(nums)-k+1):
            start=i
            end=i+k-1
            if nums[end] not in new_dict:
                new_dict[nums[end]]=1
            else:
                new_dict[nums[end]]+=1
            if new_dict[nums[start-1]]>1:
                new_dict[nums[start-1]]-=1
            else:
                del new_dict[nums[start-1]]
            cal_sum+=nums[end]
            cal_sum-=nums[start-1]
            if len(new_dict)>=m:
                max_sum=max(max_sum,cal_sum)
        return max_sum