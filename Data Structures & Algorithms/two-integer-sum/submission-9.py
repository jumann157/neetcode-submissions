class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        for a in nums:
            pos = nums.index(a)
            for b in range(pos + 1, len(nums)):
                if target - a == nums[b]:
                    answer.append(pos)
                    answer.append(b)
                    return answer
        

        