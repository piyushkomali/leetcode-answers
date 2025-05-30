class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = 0
        maxSum = nums[0]
        curSum = 0

        for r in range(len(nums)):
            curSum += nums[r]
            maxSum = max(maxSum, curSum)


            if curSum <= 0: 
                curSum = 0
                l = r
        return maxSum