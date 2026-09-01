class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_cap = 0
        a, b = 0, len(heights) - 1

        while b > a:
            height = min(heights[a], heights[b])
            width = b - a
            vol = height * width
            max_cap = max(vol, max_cap)

            if heights[b] <= heights[a]:
                b -= 1
            else:
                a += 1
        return max_cap