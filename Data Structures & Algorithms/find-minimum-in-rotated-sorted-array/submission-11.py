class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        seenMin =  nums[0]
        while l<=r:
            m = (l+r)//2
            seenMin =  min(seenMin,nums[m])
            if nums[l] < nums[r]:
                seenMin = min(nums[l],seenMin)
                break
            elif nums[m] >= nums[l]:
                l= m+1
            else:
                r = m-1
        return seenMin

