class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        elements_dict = {}

        for i in range(len(numbers)):
            sub = target - numbers[i]
            if sub in elements_dict:
                return [elements_dict[sub], i + 1]
            else:
                elements_dict[numbers[i]] = i + 1

        