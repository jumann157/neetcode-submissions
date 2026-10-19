class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        # Step 1: Find pivot
        def binarySearch():
            l, r = 0, len(nums) - 1
            while r > l:
                m = (l + r)//2
                
                if nums[m] > nums[r]:
                    l = m + 1
                elif nums[m] < nums[r]:
                    r = m
            return nums[l], l

        pivot, p_index = binarySearch()
        print(f"pivot: {pivot}, p_index: {p_index}")

        # Step 2: Find new range (left or right to pivot OR pivot is target)
        if pivot == target:
            return p_index
        
        if target > nums[r]:
            r = p_index - 1
        elif target < nums[r]:
            l = p_index + 1


        print(f"new r: {r}, l: {l}")
        while r >= l:
            m = (l + r)//2
            print(f"m: {m}")

            if nums[m] == target:
                return m
            
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1

        # if nothing is found
        return -1


