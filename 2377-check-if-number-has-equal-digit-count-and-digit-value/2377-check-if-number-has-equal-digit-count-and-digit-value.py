class Solution:
    def digitCount(self, num: str) -> bool:
        new_dict={}
        for i in num:
            if i in new_dict:
                new_dict[i]+=1
            else:
                new_dict[i]=1
        for i in range(0,len(num)):
            expected = int(num[i])
            actual = new_dict.get(str(i), 0)  # use str(i) for key
            if expected != actual:
                return False
        return True
        