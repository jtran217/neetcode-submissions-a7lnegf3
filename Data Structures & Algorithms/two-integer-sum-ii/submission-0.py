class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointers left and right.
        # sum them. if sum > target r-=1
        # sum < target l += 1
        # if sum == target return [l,r]

        l,r = 0 ,len(numbers)-1

        while l<r:
            total = numbers[l] + numbers[r]
            if total == target:
                return [l+1,r+1]
            if total > target:
                r -= 1
            else:
                l += 1
        