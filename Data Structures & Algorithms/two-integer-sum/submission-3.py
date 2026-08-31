class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i,num in enumerate(nums):
            compliment = target - num
            if not (compliment in seen):
                seen[num] = i
            else:
                return [seen[compliment],i]