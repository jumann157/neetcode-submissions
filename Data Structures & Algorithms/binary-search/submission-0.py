class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        # -1 0 2 4 6 8 10
        # s             e
        # t = 4
        while end >= start:
            middle = int((end - start) / 2 + start)
            if target > nums[middle]:
                start = middle + 1
            elif target < nums[middle]:
                end = middle - 1
            else:
                return middle
        return -1

