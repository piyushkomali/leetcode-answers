# objective - see if 2 numbers in the array sum to the target

#to solve this problem you need to initialize a map to store all values you have read so far
# then, you need to iterate over the array and see if [this value(nums[i]) + a value you have put in the map] sum to the target 
# if that value is in the map then you return the location in the arrays where these 2 values exist, so i and whatever index the map value matches
# if there is no value in the map [ for the first iteration there wont be] you can add num[i] to map
# KEY POINT: because you cannot search a key with its value in a map you will instead need to make [ key = array value, value = index] 
#            this is because you need to return the indices not values

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i in range(len(nums)):
            if ((target - nums[i]) in map):
                return {map.get(target - nums[i]), i}
            
            map[nums[i]] = i

        
        return {}
