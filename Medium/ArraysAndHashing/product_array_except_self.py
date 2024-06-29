class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = [[] for i in range(len(nums))]

        prefix = 1

        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        # result = [[], [], [], []]
        # result[0] = 1
        # [1, [], [], []]
        # 1 *= 1

        # prefix = 1
        # result[1] = 1
        # [1, 1, [], []]
        # 1 *= 2

        # prefix = 2
        # result[2] = 2
        # [1, 1, 2, []]
        # 2 *= 3 
        
        # prefix = 6
        # result[3] = 6
        # [1, 1, 2, 6]
        # exit loop

        postfix = 1

        for i in range(len(nums) -1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        # [1, 1, 2, 6]
        # nums = [1, 2, 3, 4]

        # result[3] *= 1
        # [1, 1, 2, 6]
        # postfix *= 4 
        # postfix = 4

        # result[2] *= 4
        # [1, 1, 8, 6]
        # postfix *= nums[2]
        # 4 *= 3
        # postfix = 12
        
        # result[1] *= 12
        # [1, 12, 8, 6]
        # postfix *= nums[1]
        # 12 *= 2
        # postfix = 24

        # result[0] *= 24
        # [24, 12, 8 , 6]
        # postfix *= nums[i]
        # postfix = 24

        # result = [24, 12, 8, 6]

        return result

        # prefix = 1
        # 
