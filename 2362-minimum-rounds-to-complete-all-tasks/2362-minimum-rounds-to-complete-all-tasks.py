class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        count=0
        new_dict={}
        for i in range(0,len(tasks)):
            if tasks[i] in new_dict:
                new_dict[tasks[i]]+=1
            else:
                new_dict[tasks[i]]=1
        for i in new_dict:
            while new_dict[i]:
                if new_dict[i]==1:
                    return -1
                if new_dict[i]%3==0:
                    new_dict[i]-=3
                else:
                    new_dict[i]-=2
                count+=1
        return count
        
        