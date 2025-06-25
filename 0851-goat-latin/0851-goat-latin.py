class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        sentence=sentence.split()
        for i in range(0,len(sentence)):
            if sentence[i][0] in 'aeiou' or sentence[i][0] in 'AEIOU':
                sentence[i]=sentence[i]+'ma'+'a'*(i+1)
            else:
                letter=sentence[i][0]
                sentence[i]=sentence[i][1:]+letter+'ma'+'a'*(i+1)
        return " ".join(sentence)
        