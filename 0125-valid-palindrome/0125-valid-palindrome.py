class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        n=''
        if s=='':
            return True
        for i in s:
            if i.isalpha() or i.isdigit():
                n+=i
        if n[::-1]==n:
            return True
        else:
            return False
        