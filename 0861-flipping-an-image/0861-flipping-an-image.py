class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(0,len(image)):
            k=0
            j=len(image[0])-1
            while k<j:
                image[i][k],image[i][j]=image[i][j],image[i][k]
                k+=1
                j-=1
        for i in range(0,len(image)):
            for j in range(0,len(image)):
                if image[i][j]==1:
                    image[i][j]=0
                else:
                    image[i][j]=1
        return image
        