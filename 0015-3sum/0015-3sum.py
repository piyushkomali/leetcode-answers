class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        retList = []
        nums.sort()

        for i, num in enumerate(nums):
            # Skip duplicate for the first element of the triplet
            if i > 0 and num == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                current_sum = num + nums[l] + nums[r]
                if current_sum > 0:
                    r -= 1
                elif current_sum < 0:
                    l += 1
                else:
                    retList.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # Skip duplicates for the second element of the triplet
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    # Skip duplicates for the third element of the triplet
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return retList