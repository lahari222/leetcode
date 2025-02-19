class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        new_dict = {}  
        for i in range(len(numbers)):  
            result = target - numbers[i]  
            if result in new_dict:  
                return [new_dict[result]+1, i+1]  # Return the indices of the two numbers
            new_dict[numbers[i]] = i  # Store the current number's index
        
        
        