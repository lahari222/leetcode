class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        for i in range(0,len(possible)):
            if possible[i]==0:
                possible[i]=-1
        prefix=[0]*len(possible)
        prefix[0]=possible[0]
        suffix=[0]*len(possible)
        suffix[-1]=possible[-1]
        for i in range(1,len(prefix)):
            prefix[i]=prefix[i-1]+possible[i]
        for i in range(len(suffix)-2,-1,-1):
            suffix[i]=suffix[i+1]+possible[i]
        for i in range(0,len(possible)-1):
            if prefix[i]>suffix[i+1]:
                return i+1
        return -1
       