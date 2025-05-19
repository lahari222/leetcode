class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        before,after=0,0
        n=len(nums)
        result=[]
        #doing prefix_sum
        prefix=[0]*len(nums)
        prefix[0]=nums[0]
        for i in range(1,len(nums)):
            prefix[i]=prefix[i-1]+nums[i]
        for i in range(0,len(nums)):
            left=i
            right=n-i-1
            if left>=k and right>=k:
                before=i-k
                after=i+k
                if before==0:
                    total_sum=prefix[after]
                else:
                    total_sum=prefix[after]-prefix[before-1]
                length=after-before+1
                total_sum=abs(total_sum//length)
                result.append(total_sum)
            else:
                result.append(-1)
        return result


        
        