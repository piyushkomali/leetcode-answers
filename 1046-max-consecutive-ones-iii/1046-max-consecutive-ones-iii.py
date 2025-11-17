class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxLen = 0
        l,r =0,0
        swaps = 0
        while r < len(nums):
            if nums[r] == 1: 
                r+=1
            else:
                if swaps < k:
                    swaps+=1
                    r+=1
                else: 
                    while nums[l] == 1:
                        l+=1
                    swaps-=1
                    l+=1
            maxLen = max(maxLen, r-l)
        return maxLen