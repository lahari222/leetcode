class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        new_array=[]
        i=0
        while i<len(nums):
            start=nums[i]
            while i<len(nums)-1 and nums[i]+1==nums[i+1]:
                i+=1
            if start!=nums[i]:
                new_array.append(f"{start}->{nums[i]}")
            else:
                new_array.append(str(nums[i]))
            i+=1
        return new_array

            


        