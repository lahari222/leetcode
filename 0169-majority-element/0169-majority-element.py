class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_count=0
        list1=set(nums)
        for i in list1:
            new=nums.count(i)
            if new>=max_count:
                max_count=new
                n=i
        return n
        