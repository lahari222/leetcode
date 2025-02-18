class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count=0
        for i in t:
            if i not in s:
                return False
                break
            if i in s:
                s=s.replace(i,'',1)
                count+=1
        if (count==len(t)) and len(s)==0:
            return True
        else:
            return False

        