class Solution:
    def twoSum(self, nums, target) :
        obj = {}
        for i,v in enumerate(nums):
            rest = target - v
            if rest in obj:
                return [obj[rest],i]
            else:
                obj[v] = i