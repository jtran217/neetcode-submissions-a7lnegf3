class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * n
        postfix = [0] * n

        # Know first position and last position in prefix,postfix respectively are 1
        prefix[0] = postfix[-1] = 1
        # populate prefix
        for i in range(1,n):
            prefix[i] = nums[i-1] * prefix[i-1]
        # Populate postfix
        for i in range(n-2, -1, -1):
            postfix[i] = nums[i+1] * postfix[i+1]
        res = []
        for i in range(n):
            res.append(prefix[i] * postfix[i])
        
        return res

