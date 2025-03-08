class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white_count=0
        min_value=float('inf')
        for i in range(0,k):
            if blocks[i]=='W':
                white_count+=1
        min_value=min(min_value,white_count)
        for i in range(1,len(blocks)-k+1):
            start=i
            end=i+k-1
            if blocks[end]=='W':
                white_count+=1
            if blocks[start-1]=='W':
                white_count-=1
            min_value=min(min_value,white_count)
        return min_value

        