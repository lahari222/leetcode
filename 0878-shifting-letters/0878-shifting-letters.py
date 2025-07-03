class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:

        suffix_sum=[0]*len(shifts)
        suffix_sum[-1]=shifts[-1]
        for i in range(len(s)-2,-1,-1):
            suffix_sum[i]=suffix_sum[i+1]+shifts[i]
        s=list(s)
        for i in range(0,len(s)):
            s[i]=chr((ord(s[i]) - ord('a') + (suffix_sum[i] % 26)) % 26 + ord('a'))
        return ''.join(s)
        
        