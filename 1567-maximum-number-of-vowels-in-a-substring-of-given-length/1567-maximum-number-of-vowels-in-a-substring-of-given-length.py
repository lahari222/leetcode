class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count=0
        n=len(s)
        new_dict={}
        max_length=float('-inf')
        for i in range(0,k):
            if s[i] in 'aeiou' and s[i] not in new_dict:
                new_dict[s[i]]=1
                count+=1
            elif s[i] in 'aeiou' and s[i] in new_dict:
                new_dict[s[i]]+=1
                count+=1
        if count>max_length:
            max_length=max(max_length,count)
        for i in range(1,n-k+1):
            start=i
            end=start+k-1
            if s[end] in 'aeiou' and s[end] not in new_dict:
                new_dict[s[end]]=1
                count+=1
            elif s[end] in 'aeiou' and s[end] in new_dict:
                new_dict[s[end]]+=1
                count+=1
            if s[start-1] in new_dict and new_dict[s[start-1]]==1:
                del new_dict[s[start-1]]
                count-=1
            if s[start-1] in new_dict and new_dict[s[start-1]]>1:
                new_dict[s[start-1]]-=1
                count-=1
            if count>max_length:
                max_length=max(max_length,count)
        return max_length