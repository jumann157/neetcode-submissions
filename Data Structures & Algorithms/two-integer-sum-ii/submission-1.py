class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a,b = 0, len(numbers) - 1
        for i in range(len(numbers)):
            sub = target - numbers[b]

            while numbers[a] <= sub and a < b:
                    if numbers[a] == sub:
                        return [a + 1, b + 1]
                    a += 1
            # a = 0  
            b -= 1 # if sub < nummbers[a], hypothetically a == 0, then no more values exist, so we go to the nect value, b--


        