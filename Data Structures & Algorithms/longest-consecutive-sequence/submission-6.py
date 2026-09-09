class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniqueChar = set(nums)
        
        maxCount = 0
        for c in uniqueChar:
            if c-1 not in uniqueChar:
                count = 0
                while c+count in uniqueChar:
                    count +=1
                maxCount = max(maxCount,count)
        return maxCount
