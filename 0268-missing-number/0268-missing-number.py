class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sExpected = (n* (n+1))/2
        sList = sum(nums)
        return int(sExpected - sList)
        