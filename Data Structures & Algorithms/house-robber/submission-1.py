class Solution:
    def rob(self, nums: List[int]) -> int:
        # Cannot rob two adjacent houses
        # Max money without alerting polic
        # Either Rob this house, or don't rob this house
        memo = {}
        def _rob(nums,i,memo):
            if i in memo:
                return memo[i]
            if i > len(nums)-1:
                return 0 
            steal = _rob(nums, i+2,memo) + nums[i]
            no_steal = _rob(nums,i+1,memo)
            profit = max(steal,no_steal) 
            memo[i] = profit

            return profit
        return _rob(nums,0,memo)