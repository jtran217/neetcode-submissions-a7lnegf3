class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # DFS every number only returning combination where target ends up at zero.
        # Store this combination in some sort of hashmap to reduce recalculations
        # Need to handle permutation

        res = []

        def dfs(i,cur,total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return
            cur.append(nums[i])
            dfs(i,cur, total + nums[i])
            cur.pop()
            dfs(i+1,cur, total)
        dfs(0,[],0)

        return res