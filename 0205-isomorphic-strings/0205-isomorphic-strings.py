class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict_1={}
        dict_2={}
        for i in range(len(s)):
            if s[i] not in dict_1:
                dict_1[s[i]]=i
            if t[i] not in dict_2:
                dict_2[t[i]]=i
            if dict_1[s[i]]!=dict_2[t[i]]:
                return False
        return True