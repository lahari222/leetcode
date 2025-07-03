class Solution:
    def replaceDigits(self, s: str) -> str:
        s=list(s)
        for i in range(1,len(s)):
            if i%2!=0:
                s[i]=chr(ord(s[i-1])+int(s[i]))
        return ''.join(s)
        


        