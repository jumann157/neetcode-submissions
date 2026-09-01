class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countMap = {} # value : count
        for x in range(len(nums)):
            value = nums[x]
            if countMap.get(value) == None:
                countMap[value] = 1
            else:
                return True
        return False