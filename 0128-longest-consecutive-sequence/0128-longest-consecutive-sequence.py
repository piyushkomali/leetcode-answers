class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = set(nums)
        checked = set()
        ret = 0
        i=0
        for i in range(len(nums)):
            if nums[i]-1 not in m and nums[i] not in checked:
                checked.add(nums[i])
                cur = 1
                start = nums[i]
                while start+1 in m:
                    cur+=1
                    start+=1
                ret = max(ret, cur)
        return ret
                


        