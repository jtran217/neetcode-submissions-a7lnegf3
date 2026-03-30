class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Take middle , consider if middle in left or right side.
        # If left then want to search right side.

        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(nums[l],res)
                break
            
            m = (l + r)//2
            res = min(res,nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res