class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        # 5 6 1 2 3 4
        while(r >= l):
            m = int((r -l)/2) + l
            print(f"l: {l}, r: {r}, m: {m}")

            if nums[m] == target:
                return m

            # left sorted
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1

            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
                

        return -1


