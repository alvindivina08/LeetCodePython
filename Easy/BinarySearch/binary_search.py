class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        # while left is less than right
        while l < r:
            # find the middle index by adding l + r divide by two
            m = (l + r) // 2
            # then find
            # if nums middle is less than target
            if nums[m] < target:
                r = m + 1
            # if nums middle is greater than target
            elif nums[m] > target:
                l = m - 1
            # if none of the above is true
            # it means we found the index of the target
            else:
                return m
                
        return -1
    
nums = [-1,0,3,5,9,12]
nums2 = [-1,0,3,5,9,12]