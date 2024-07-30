from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1

        while top <= bot:
            # calculate the middle pointer by adding top and bot divided by 2
            row = (top + bot) // 2
            # if target is larger than the last number in current row
            if target > matrix[row][-1]:
                # move the top pointer by 1
                top = row + 1
            # else if target is less than the first number in current row
            elif target < matrix[row][0]:
                # move the bottom pointer to the row - 1 (above it)
                bot = row - 1
            # else if the target is in the row
            else:
                break
        # if row is not found, return False
        if not (top <= bot):
            return False

        row = (top + bot) // 2
        l, r = 0, COLS - 1

        # now execute the two pointer binary search
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False
    
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
matrix2 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]