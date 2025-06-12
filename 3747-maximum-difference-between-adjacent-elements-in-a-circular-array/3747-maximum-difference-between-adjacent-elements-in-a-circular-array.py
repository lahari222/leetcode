class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        first_ele=nums[0]
        last_ele=nums[-1]
        max_ele=float('-inf')
        for i in range(0,len(nums)-1):
            absolute=abs(nums[i]-nums[i+1])
            max_ele=max(max_ele,absolute)
        max_ele=max(max_ele,abs(first_ele-last_ele))
        return max_ele

        