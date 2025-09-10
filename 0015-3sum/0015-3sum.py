class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        retList = set()
        def twoSum2(nums,target):
            l,r = 0, len(nums)-1
            while (l < r):
                if nums[l] + nums[r] < target: l+=1
                elif nums[l] + nums[r] > target: r-=1
                else: 
                    retList.add(tuple([-1* target, nums[l],nums[r]]))
                    l+=1
                    r-=1
            return []
        nums = sorted(nums)
        for i in range(len(nums)):
            l = twoSum2(nums[i+1:], -1 * nums[i])
        return list(retList)



