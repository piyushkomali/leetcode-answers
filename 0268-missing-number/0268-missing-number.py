class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        should = (n * (n+1)) // 2
        sumList = sum(nums)
        return should - sumList
        