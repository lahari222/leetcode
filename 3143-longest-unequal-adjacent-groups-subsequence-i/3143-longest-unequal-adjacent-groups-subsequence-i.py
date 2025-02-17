class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        i = 0
        n = len(words)
        ans = []
        while i < n:
            ans.append(words[i])
            while i < n-1 and groups[i] == groups[i+1]:
                i += 1
            i += 1
        return ans


        