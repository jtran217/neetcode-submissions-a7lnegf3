class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        
        for num in nums:
            if num:
                product *= num
            else:
                zero_count += 1
        if zero_count > 1:return[0] * len(nums)

        result = [0] * len(nums)
        for i,n in enumerate(nums):
            if zero_count: result[i] = 0 if n else product
            else: result[i] = product //n
        return result