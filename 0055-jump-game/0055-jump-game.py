class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        while i < len(nums)-1:
            if nums[i] == 0: return False
            curJump = nums[i]
            j = 0

            while i < len(nums)-1 and j < curJump:
                i+=1
                j+=1
                if j + nums[i] > curJump: 
                    curJump = nums[i]
                    j=0
        if i >= len(nums)-1: return True
        return False
            
