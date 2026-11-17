class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        map={}
        for i in range(0,len(nums)):
            diff=target-nums[i]
            if diff in map:
                return [map[diff],i]
            map[nums[i]]=i
        
