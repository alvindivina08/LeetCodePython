from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            number = numbers[r] + numbers[l]

            if number == target:
                return [l + 1, r + 1]
            
            if number < target:
                l += 1
            else:
                r -= 1
        
        return 
