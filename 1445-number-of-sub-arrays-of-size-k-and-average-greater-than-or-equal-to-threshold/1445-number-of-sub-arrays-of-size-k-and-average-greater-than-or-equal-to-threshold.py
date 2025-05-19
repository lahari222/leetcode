class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n=len(arr)
        count=0
        window_sum=0
        for i in range(0,k):
            window_sum+=arr[i]
        if abs(window_sum//k)>=threshold:
            count+=1
        for i in range(1,n-k+1):
            start=i
            end=start+k-1
            window_sum=window_sum+arr[end]-arr[start-1]
            if abs(window_sum//k)>=threshold:
                count+=1
        return count

       
        