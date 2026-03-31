class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # min between two hights chosen
        # Move pointer with the lower height, cause we want to maximize this

        mArea = 0

        l,r = 0, len(heights) - 1

        while l < r:
            length = r - l
            height = min(heights[l],heights[r])
            mArea = max(mArea, height * length)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
            
        
        return mArea