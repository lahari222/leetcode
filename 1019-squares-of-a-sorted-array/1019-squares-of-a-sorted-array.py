class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new_list=[i*i for i in nums]
        new_list.sort()
        return new_list
        