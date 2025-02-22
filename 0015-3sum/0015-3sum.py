class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        n = len(nums)
        for i in range(n):
            l = i+1
            r = n-1
            while l < r:
                summ = nums[i] + nums[l] + nums[r]
                if summ == 0:
                    res.add((nums[i], nums[l], nums[r]))
                    l+= 1
                    r-= 1
                elif summ < 0:
                    l+= 1
                elif summ > 0:
                    r-= 1
        return list(res)



        

        