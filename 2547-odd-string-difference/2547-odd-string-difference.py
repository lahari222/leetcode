class Solution:
    def oddString(self, words: List[str]) -> str:
        n=len(words)
        m=len(words[0])
        new_dict={}
        for i in range(0,n):
            curr=[]
            for j in range(0,m-1):
                result=ord(words[i][j+1])-ord(words[i][j])
                curr.append(result)
            if tuple(curr) in new_dict:
                new_dict[tuple(curr)].append(words[i])
            else:
                new_dict[tuple(curr)]=[words[i]]
        for k,v in new_dict.items():
            if len(v)==1:
                return v[0]
            
        
        
        