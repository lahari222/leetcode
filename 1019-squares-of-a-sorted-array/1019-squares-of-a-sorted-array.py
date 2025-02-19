class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new_list=[]
        left=0
        right=len(nums)-1
        while left<=right:
            if abs(nums[left])>abs(nums[right]):
                new_list.append(nums[left]*nums[left])
                left+=1
            else:
                new_list.append(nums[right]*nums[right])
                right-=1
        return new_list[::-1]
        