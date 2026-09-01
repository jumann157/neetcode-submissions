class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        d = {} # 4:0
        for a in range(len(nums)):
            value = nums[a]
            sub = target - value 
            if sub in d:
                answer.append(d[sub])
                answer.append(a)
                return answer

            d[value ] = a
        

        