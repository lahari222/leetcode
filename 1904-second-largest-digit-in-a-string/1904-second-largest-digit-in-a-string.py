class Solution:
    def secondHighest(self, s: str) -> int:
        new_dict={}
        for i in s:
            if i.isnumeric():
                if i in new_dict:
                    new_dict[int(i)]+=1
                else:
                    new_dict[int(i)]=1
        if len(new_dict)==1 or len(new_dict)==0:
            return -1
        first_max=next(iter(new_dict))
        second_max=float('-inf')
        for k,v in new_dict.items():
            if k>first_max:
                second_max=first_max
                first_max=k
            if k<first_max and k>second_max:
                second_max=k
        return second_max

        
            
        