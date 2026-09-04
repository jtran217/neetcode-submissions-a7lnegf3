class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # value:index

        for index,num in enumerate(nums):
            complimentary = target - num

            if complimentary in seen:
                return [seen[complimentary],index]
            seen[num] = index
        
        return []