class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i=0
        j=len(nums)-1
        while i<=j:
            if(nums[i]<target):
                i+=1
            elif(nums[i]>target):
                j-=1
            elif(nums[i]==target):
                return i
            elif(nums[j]==target):
                return j
        return -1
        