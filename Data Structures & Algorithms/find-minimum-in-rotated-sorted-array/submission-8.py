class Solution:
    def findMin(self, nums: List[int]) -> int:
        seen = nums[0]

        l,r = 0, len(nums)-1
        
        while l<=r:
            if(nums[l] <= nums[r]):
                seen = min(seen,nums[l])
                break
            m = (l+r)//2
            seen = min(seen,nums[m])

            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return seen