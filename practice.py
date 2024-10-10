sentence = "Hello, world!"

def countString(string):
    count = {}

    for n in string:
        if n.isalnum():
            count[n] = count.get(n, 0) + 1

    return count

# result = countString(sentence)

# print(result)

json = {
    "fruits": ["apple", "orange", "banana"],
    "vegetables": ["onion", "bell pepper"]
}

def addData(jsonDoc, key, item):

    if key in jsonDoc:
        jsonDoc[key].append(item)
    else:
        jsonDoc[key] = [item]

    return jsonDoc

# result = addData(json, 'yeet', 'potato')
# result = addData(json, 'yeet', 'jingle bells')


# print(result)


from typing import List
class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1

        # if target is greater than the last number of the current row
            # then increment top by adding 1 to row
        # else if the target is less than the first number in the current row
            # then decrement row = bottom by 1

        while top <= bot:
            row = (top + bot) // 2
            print(row)
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        
        if not (top <= bot):
            return False
        
        row = (top + bot) // 2
        l, r = 0, COLS - 1

        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        
        return False

solution = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]

result = solution.searchMatrix(matrix, 3)
print(result)