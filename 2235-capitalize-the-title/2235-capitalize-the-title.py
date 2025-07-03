class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title=title.split()
        for i in range(0,len(title)):
            if len(title[i])>2:
                title[i]=title[i].capitalize()
            else:
                title[i]=title[i].lower()
        return " ".join(title)

                
        