class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        total=0
        sum_sub=[]
        #creating prefix_sum
        for i in range(1,n):
            nums[i]=nums[i-1]+nums[i]
        for i in range(0,n):
            for j in range(i,n):
                if i==0:
                    total_sum=nums[j]
                    sum_sub.append(total_sum)
                else:
                    total_sum=nums[j]-nums[i-1]
                    sum_sub.append(total_sum)
        sum_sub.sort()
        return sum(sum_sub[left-1:right])%(10**9+7)
                    
                

        