class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Store what we seen in dictionary
        # Calc needed number and see if in seen dictionary 
        # Return index if seen

        seen = {}

        for i,n in enumerate(numbers):
            pair = target - n
            if pair in seen:
                return [seen[pair]+1,i+1]
            seen[n] = i 
        
        