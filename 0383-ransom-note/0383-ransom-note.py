class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count=0
        for i in ransomNote:
            if i in magazine:
                magazine=magazine.replace(i,'',1)
                count+=1
        return count==len(ransomNote)
        
        