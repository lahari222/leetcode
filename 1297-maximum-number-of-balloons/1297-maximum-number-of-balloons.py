class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        new_dict = {}
        for i in text:
            if i in 'balloon':
                new_dict[i] = new_dict.get(i, 0) + 1

        return min(new_dict.get("b", 0), 
                   new_dict.get("a", 0), 
                   new_dict.get("l", 0) // 2, 
                   new_dict.get("o", 0) // 2, 
                   new_dict.get("n", 0))