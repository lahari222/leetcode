class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        new_str=sentence.split()
        for i in range(0,len(new_str)):
            if new_str[i].startswith(searchWord):
                return i+1
        return -1