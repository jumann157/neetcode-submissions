class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        post = 1
        pre = 1

        # prefix filling
        for i in range(len(nums)):
            output.insert(i, pre)
            pre *= nums[i]
        
        # postfix filling
        for x in range(len(nums) - 1, -1, -1):
            output[x] *= post
            post *= nums[x]
        
        return output