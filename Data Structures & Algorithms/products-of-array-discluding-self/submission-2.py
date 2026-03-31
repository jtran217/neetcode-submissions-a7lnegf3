class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_cnt = 0

        for n in nums:
            if n:
                product *= n
            else:
                zero_cnt += 1
        
        if zero_cnt > 1:
            return [0] * len(nums)
        
        res = [0] * len(nums)
        for i,c in enumerate(nums):
            if zero_cnt:
                if c:
                    res[i] = 0
                else:
                    res[i] = product
            else:
                res[i] = product//c
        return res
        
