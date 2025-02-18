class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        new_dict={}
        ans=0
        for i in stones:
            if (i in jewels):
                if i in new_dict:
                    new_dict[i]+=1
                else:
                    new_dict[i]=1
        for k,v in new_dict.items():
            ans+=v
        return ans

            
        