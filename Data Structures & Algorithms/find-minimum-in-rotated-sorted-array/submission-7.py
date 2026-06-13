class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        seenMin = nums[0]
        l,r = 0,len(nums)-1

        while l<=r:
            m = (l+r) // 2

            if nums[l] <= nums[r]:
                seenMin = min(seenMin,nums[l])
                break
            seenMin = min(seenMin, nums[m])
            
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        
        return seenMin