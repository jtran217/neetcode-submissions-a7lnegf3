class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Two pointer
        # min of the two is used as height 
        # distance between l and r is the length
        # area = l x h
        # Pointer change condition is to increment the lower value one. 

        l = 0
        r = len(heights) - 1
        mWater = 0

        while l<r:
            h = min(heights[l],heights[r])
            w = (r - l)
            area = h * w
            mWater = max(mWater,area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return mWater