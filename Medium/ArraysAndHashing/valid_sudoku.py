from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # here we are creating a dictionary to save the numbers we have seen on
        # rows
        # cols
        # and squares

        # we are basically saving the coordinates of the numbers we have seen in the board

        """
        The default initializer prevents you from getting the KeyError and instead does whatever you tell it to in the defaultdict constructor. 
        This is also handy when you want a dictionary of lists, or a dictionary of dictionaries, and so on.
        """
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        # this is how we traverse the board
        # as long as we know how big the board is
        # we are gonna hardcode it
        for r in range(9):
            for c in range(9):
                print(board[r][c], r, c)
                if board[r][c] == ".":
                    continue
                
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                
                # why do we need to add this to rows[r], cols[c] and squares[(r //3, c// 3)] ?
                # so that we dont blindly save it in an array.
                #  we want it to be inside mapped! array
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[( r // 3, c // 3)].add(board[r][c])

                print("\n")
                print(rows)
                print("\n")
                print(cols)
                print("\n")
                print(squares)
                print("\n")

            
        
        return True
    

"""
[
["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]
]

b r c
5 0 0


defaultdict(<class 'set'>, {0: {'5'}})


defaultdict(<class 'set'>, {0: {'5'}})


defaultdict(<class 'set'>, {(0, 0): {'5'}})


3 0 1


defaultdict(<class 'set'>, {0: {'3', '5'}})


defaultdict(<class 'set'>, {0: {'5'}, 1: {'3'}})


defaultdict(<class 'set'>, {(0, 0): {'3', '5'}})


. 0 2
. 0 3
7 0 4


defaultdict(<class 'set'>, {0: {'7', '3', '5'}})


defaultdict(<class 'set'>, {0: {'5'}, 1: {'3'}, 4: {'7'}})


defaultdict(<class 'set'>, {(0, 0): {'3', '5'}, (0, 1): {'7'}})


. 0 5
. 0 6
. 0 7
. 0 8
6 1 0


defaultdict(<class 'set'>, {0: {'7', '3', '5'}, 1: {'6'}})


defaultdict(<class 'set'>, {0: {'6', '5'}, 1: {'3'}, 4: {'7'}})


defaultdict(<class 'set'>, {(0, 0): {'6', '3', '5'}, (0, 1): {'7'}})


. 1 1
. 1 2
1 1 3


defaultdict(<class 'set'>, {0: {'7', '3', '5'}, 1: {'6', '1'}})


defaultdict(<class 'set'>, {0: {'6', '5'}, 1: {'3'}, 4: {'7'}, 3: {'1'}})


defaultdict(<class 'set'>, {(0, 0): {'6', '3', '5'}, (0, 1): {'7', '1'}})


9 1 4


defaultdict(<class 'set'>, {0: {'7', '3', '5'}, 1: {'6', '1', '9'}})


defaultdict(<class 'set'>, {0: {'6', '5'}, 1: {'3'}, 4: {'7', '9'}, 3: {'1'}})


defaultdict(<class 'set'>, {(0, 0): {'6', '3', '5'}, (0, 1): {'7', '1', '9'}})


5 1 5


defaultdict(<class 'set'>, {0: {'7', '3', '5'}, 1: {'6', '1', '9', '5'}})


defaultdict(<class 'set'>, {0: {'6', '5'}, 1: {'3'}, 4: {'7', '9'}, 3: {'1'}, 5: {'5'}})


defaultdict(<class 'set'>, {(0, 0): {'6', '3', '5'}, (0, 1): {'7', '1', '9', '5'}})


. 1 6
. 1 7
. 1 8
. 2 0
9 2 1


defaultdict(<class 'set'>, {0: {'7', '3', '5'}, 1: {'6', '1', '9', '5'}, 2: {'9'}})


defaultdict(<class 'set'>, {0: {'6', '5'}, 1: {'9', '3'}, 4: {'7', '9'}, 3: {'1'}, 5: {'5'}})


defaultdict(<class 'set'>, {(0, 0): {'6', '9', '3', '5'}, (0, 1): {'7', '1', '9', '5'}})


8 2 2


defaultdict(<class 'set'>, {0: {'7', '3', '5'}, 1: {'6', '1', '9', '5'}, 2: {'8', '9'}})


defaultdict(<class 'set'>, {0: {'6', '5'}, 1: {'9', '3'}, 4: {'7', '9'}, 3: {'1'}, 5: {'5'}, 2: {'8'}})


defaultdict(<class 'set'>, {(0, 0): {'6', '9', '8', '3', '5'}, (0, 1): {'7', '1', '9', '5'}})


. 2 3
. 2 4
. 2 5
. 2 6
6 2 7


defaultdict(<class 'set'>, {0: {'7', '3', '5'}, 1: {'6', '1', '9', '5'}, 2: {'8', '6', '9'}})


defaultdict(<class 'set'>, {0: {'6', '5'}, 1: {'9', '3'}, 4: {'7', '9'}, 3: {'1'}, 5: {'5'}, 2: {'8'}, 7: {'6'}})


defaultdict(<class 'set'>, {(0, 0): {'6', '9', '8', '3', '5'}, (0, 1): {'7', '1', '9', '5'}, (0, 2): {'6'}})


. 2 8
8 3 0


defaultdict(<class 'set'>, {0: {'7', '3', '5'}, 1: {'6', '1', '9', '5'}, 2: {'8', '6', '9'}, 3: {'8'}})


defaultdict(<class 'set'>, {0: {'6', '8', '5'}, 1: {'9', '3'}, 4: {'7', '9'}, 3: {'1'}, 5: {'5'}, 2: {'8'}, 7: {'6'}})


defaultdict(<class 'set'>, {(0, 0): {'6', '9', '8', '3', '5'}, (0, 1): {'7', '1', '9', '5'}, (0, 2): {'6'}, (1, 0): {'8'}})


. 3 1
. 3 2
. 3 3
6 3 4


defaultdict(<class 'set'>, {0: {'7', '3', '5'}, 1: {'6', '1', '9', '5'}, 2: {'8', '6', '9'}, 3: {'8', '6'}})


defaultdict(<class 'set'>, {0: {'6', '8', '5'}, 1: {'9', '3'}, 4: {'6', '7', '9'}, 3: {'1'}, 5: {'5'}, 2: {'8'}, 7: {'6'}})


defaultdict(<class 'set'>, {(0, 0): {'6', '9', '8', '3', '5'}, (0, 1): {'7', '1', '9', '5'}, (0, 2): {'6'}, (1, 0): {'8'}, (1, 1): {'6'}})


. 3 5
. 3 6
. 3 7
3 3 8


defaultdict(<class 'set'>, {0: {'7', '3', '5'}, 1: {'6', '1', '9', '5'}, 2: {'8', '6', '9'}, 3: {'8', '6', '3'}})


defaultdict(<class 'set'>, {0: {'6', '8', '5'}, 1: {'9', '3'}, 4: {'6', '7', '9'}, 3: {'1'}, 5: {'5'}, 2: {'8'}, 7: {'6'}, 8: {'3'}})


defaultdict(<class 'set'>, {(0, 0): {'6', '9', '8', '3', '5'}, (0, 1): {'7', '1', '9', '5'}, (0, 2): {'6'}, (1, 0): {'8'}, (1, 1): {'6'}, (1, 2): {'3'}})


4 4 0


defaultdict(<class 'set'>, {0: {'7', '3', '5'}, 1: {'6', '1', '9', '5'}, 2: {'8', '6', '9'}, 3: {'8', '6', '3'}, 4: {'4'}})


defaultdict(<class 'set'>, {0: {'6', '4', '8', '5'}, 1: {'9', '3'}, 4: {'6', '7', '9'}, 3: {'1'}, 5: {'5'}, 2: {'8'}, 7: {'6'}, 8: {'3'}})


defaultdict(<class 'set'>, {(0, 0): {'6', '9', '8', '3', '5'}, (0, 1): {'7', '1', '9', '5'}, (0, 2): {'6'}, (1, 0): {'8', '4'}, (1, 1): {'6'}, (1, 2): {'3'}})


. 4 1
. 4 2
8 4 3


defaultdict(<class 'set'>, {0: {'7', '3', '5'}, 1: {'6', '1', '9', '5'}, 2: {'8', '6', '9'}, 3: {'8', '6', '3'}, 4: {'8', '4'}})


defaultdict(<class 'set'>, {0: {'6', '4', '8', '5'}, 1: {'9', '3'}, 4: {'6', '7', '9'}, 3: {'8', '1'}, 5: {'5'}, 2: {'8'}, 7: {'6'}, 8: {'3'}})


defaultdict(<class 'set'>, {(0, 0): {'6', '9', '8', '3', '5'}, (0, 1): {'7', '1', '9', '5'}, (0, 2): {'6'}, (1, 0): {'8', '4'}, (1, 1): {'6', '8'}, (1, 2): {'3'}})


. 4 4
3 4 5


defaultdict(<class 'set'>, {0: {'7', '3', '5'}, 1: {'6', '1', '9', '5'}, 2: {'8', '6', '9'}, 3: {'8', '6', '3'}, 4: {'8', '4', '3'}})


defaultdict(<class 'set'>, {0: {'6', '4', '8', '5'}, 1: {'9', '3'}, 4: {'6', '7', '9'}, 3: {'8', '1'}, 5: {'3', '5'}, 2: {'8'}, 7: {'6'}, 8: {'3'}})


defaultdict(<class 'set'>, {(0, 0): {'6', '9', '8', '3', '5'}, (0, 1): {'7', '1', '9', '5'}, (0, 2): {'6'}, (1, 0): {'8', '4'}, (1, 1): {'6', '3', '8'}, (1, 2): {'3'}})


. 4 6
. 4 7
1 4 8


defaultdict(<class 'set'>, {0: {'7', '3', '5'}, 1: {'6', '1', '9', '5'}, 2: {'8', '6', '9'}, 3: {'8', '6', '3'}, 4: {'8', '4', '1', '3'}})


defaultdict(<class 'set'>, {0: {'6', '4', '8', '5'}, 1: {'9', '3'}, 4: {'6', '7', '9'}, 3: {'8', '1'}, 5: {'3', '5'}, 2: {'8'}, 7: {'6'}, 8: {'1', '3'}})


defaultdict(<class 'set'>, {(0, 0): {'6', '9', '8', '3', '5'}, (0, 1): {'7', '1', '9', '5'}, (0, 2): {'6'}, (1, 0): {'8', '4'}, (1, 1): {'6', '3', '8'}, (1, 2): {'1', '3'}})


7 5 0


defaultdict(<class 'set'>, {0: {'7', '3', '5'}, 1: {'6', '1', '9', '5'}, 2: {'8', '6', '9'}, 3: {'8', '6', '3'}, 4: {'8', '4', '1', '3'}, 5: {'7'}})


defaultdict(<class 'set'>, {0: {'6', '7', '8', '4', '5'}, 1: {'9', '3'}, 4: {'6', '7', '9'}, 3: {'8', '1'}, 5: {'3', '5'}, 2: {'8'}, 7: {'6'}, 8: {'1', '3'}})


defaultdict(<class 'set'>, {(0, 0): {'6', '9', '8', '3', '5'}, (0, 1): {'7', '1', '9', '5'}, (0, 2): {'6'}, (1, 0): {'8', '7', '4'}, (1, 1): {'6', '3', '8'}, (1, 2): {'1', '3'}})


. 5 1
. 5 2
. 5 3
2 5 4


defaultdict(<class 'set'>, {0: {'7', '3', '5'}, 1: {'6', '1', '9', '5'}, 2: {'8', '6', '9'}, 3: {'8', '6', '3'}, 4: {'8', '4', '1', '3'}, 5: {'2', '7'}})


defaultdict(<class 'set'>, {0: {'6', '7', '8', '4', '5'}, 1: {'9', '3'}, 4: {'6', '7', '2', '9'}, 3: {'8', '1'}, 5: {'3', '5'}, 2: {'8'}, 7: {'6'}, 8: {'1', '3'}})


defaultdict(<class 'set'>, {(0, 0): {'6', '9', '8', '3', '5'}, (0, 1): {'7', '1', '9', '5'}, (0, 2): {'6'}, (1, 0): {'8', '7', '4'}, (1, 1): {'6', '2', '3', '8'}, (1, 2): {'1', '3'}})


. 5 5
. 5 6
. 5 7
6 5 8


defaultdict(<class 'set'>, {0: {'7', '3', '5'}, 1: {'6', '1', '9', '5'}, 2: {'8', '6', '9'}, 3: {'8', '6', '3'}, 4: {'8', '4', '1', '3'}, 5: {'2', '7', '6'}})


defaultdict(<class 'set'>, {0: {'6', '7', '8', '4', '5'}, 1: {'9', '3'}, 4: {'6', '7', '2', '9'}, 3: {'8', '1'}, 5: {'3', '5'}, 2: {'8'}, 7: {'6'}, 8: {'6', '1', '3'}})


defaultdict(<class 'set'>, {(0, 0): {'6', '9', '8', '3', '5'}, (0, 1): {'7', '1', '9', '5'}, (0, 2): {'6'}, (1, 0): {'8', '7', '4'}, (1, 1): {'6', '2', '3', '8'}, (1, 2): {'6', '1', '3'}})


. 6 0
6 6 1


defaultdict(<class 'set'>, {0: {'7', '3', '5'}, 1: {'6', '1', '9', '5'}, 2: {'8', '6', '9'}, 3: {'8', '6', '3'}, 4: {'8', '4', '1', '3'}, 5: {'2', '7', '6'}, 6: {'6'}})


defaultdict(<class 'set'>, {0: {'6', '7', '8', '4', '5'}, 1: {'6', '9', '3'}, 4: {'6', '7', '2', '9'}, 3: {'8', '1'}, 5: {'3', '5'}, 2: {'8'}, 7: {'6'}, 8: {'6', '1', '3'}})


defaultdict(<class 'set'>, {(0, 0): {'6', '9', '8', '3', '5'}, (0, 1): {'7', '1', '9', '5'}, (0, 2): {'6'}, (1, 0): {'8', '7', '4'}, (1, 1): {'6', '2', '3', '8'}, (1, 2): {'6', '1', '3'}, (2, 0): {'6'}})


. 6 2
. 6 3
. 6 4
. 6 5
2 6 6


defaultdict(<class 'set'>, {0: {'7', '3', '5'}, 1: {'6', '1', '9', '5'}, 2: {'8', '6', '9'}, 3: {'8', '6', '3'}, 4: {'8', '4', '1', '3'}, 5: {'2', '7', '6'}, 6: {'6', '2'}})


defaultdict(<class 'set'>, {0: {'6', '7', '8', '4', '5'}, 1: {'6', '9', '3'}, 4: {'6', '7', '2', '9'}, 3: {'8', '1'}, 5: {'3', '5'}, 2: {'8'}, 7: {'6'}, 8: {'6', '1', '3'}, 6: {'2'}})


defaultdict(<class 'set'>, {(0, 0): {'6', '9', '8', '3', '5'}, (0, 1): {'7', '1', '9', '5'}, (0, 2): {'6'}, (1, 0): {'8', '7', '4'}, (1, 1): {'6', '2', '3', '8'}, (1, 2): {'6', '1', '3'}, (2, 0): {'6'}, (2, 2): {'2'}})


8 6 7


defaultdict(<class 'set'>, {0: {'7', '3', '5'}, 1: {'6', '1', '9', '5'}, 2: {'8', '6', '9'}, 3: {'8', '6', '3'}, 4: {'8', '4', '1', '3'}, 5: {'2', '7', '6'}, 6: {'6', '2', '8'}})


defaultdict(<class 'set'>, {0: {'6', '7', '8', '4', '5'}, 1: {'6', '9', '3'}, 4: {'6', '7', '2', '9'}, 3: {'8', '1'}, 5: {'3', '5'}, 2: {'8'}, 7: {'6', '8'}, 8: {'6', '1', '3'}, 6: {'2'}})


defaultdict(<class 'set'>, {(0, 0): {'6', '9', '8', '3', '5'}, (0, 1): {'7', '1', '9', '5'}, (0, 2): {'6'}, (1, 0): {'8', '7', '4'}, (1, 1): {'6', '2', '3', '8'}, (1, 2): {'6', '1', '3'}, (2, 0): {'6'}, (2, 2): {'2', '8'}})


. 6 8
. 7 0
. 7 1
. 7 2
4 7 3


defaultdict(<class 'set'>, {0: {'7', '3', '5'}, 1: {'6', '1', '9', '5'}, 2: {'8', '6', '9'}, 3: {'8', '6', '3'}, 4: {'8', '4', '1', '3'}, 5: {'2', '7', '6'}, 6: {'6', '2', '8'}, 7: {'4'}})


defaultdict(<class 'set'>, {0: {'6', '7', '8', '4', '5'}, 1: {'6', '9', '3'}, 4: {'6', '7', '2', '9'}, 3: {'8', '4', '1'}, 5: {'3', '5'}, 2: {'8'}, 7: {'6', '8'}, 8: {'6', '1', '3'}, 6: {'2'}})


defaultdict(<class 'set'>, {(0, 0): {'6', '9', '8', '3', '5'}, (0, 1): {'7', '1', '9', '5'}, (0, 2): {'6'}, (1, 0): {'8', '7', '4'}, (1, 1): {'6', '2', '3', '8'}, (1, 2): {'6', '1', '3'}, (2, 0): {'6'}, (2, 2): {'2', '8'}, (2, 1): {'4'}})


1 7 4


defaultdict(<class 'set'>, {0: {'7', '3', '5'}, 1: {'6', '1', '9', '5'}, 2: {'8', '6', '9'}, 3: {'8', '6', '3'}, 4: {'8', '4', '1', '3'}, 5: {'2', '7', '6'}, 6: {'6', '2', '8'}, 7: {'4', '1'}})


defaultdict(<class 'set'>, {0: {'6', '7', '8', '4', '5'}, 1: {'6', '9', '3'}, 4: {'6', '1', '9', '7', '2'}, 3: {'8', '4', '1'}, 5: {'3', '5'}, 2: {'8'}, 7: {'6', '8'}, 8: {'6', '1', '3'}, 6: {'2'}})


defaultdict(<class 'set'>, {(0, 0): {'6', '9', '8', '3', '5'}, (0, 1): {'7', '1', '9', '5'}, (0, 2): {'6'}, (1, 0): {'8', '7', '4'}, (1, 1): {'6', '2', '3', '8'}, (1, 2): {'6', '1', '3'}, (2, 0): {'6'}, (2, 2): {'2', '8'}, (2, 1): {'4', '1'}})


9 7 5


defaultdict(<class 'set'>, {0: {'7', '3', '5'}, 1: {'6', '1', '9', '5'}, 2: {'8', '6', '9'}, 3: {'8', '6', '3'}, 4: {'8', '4', '1', '3'}, 5: {'2', '7', '6'}, 6: {'6', '2', '8'}, 7: {'4', '1', '9'}})


defaultdict(<class 'set'>, {0: {'6', '7', '8', '4', '5'}, 1: {'6', '9', '3'}, 4: {'6', '1', '9', '7', '2'}, 3: {'8', '4', '1'}, 5: {'9', '3', '5'}, 2: {'8'}, 7: {'6', '8'}, 8: {'6', '1', '3'}, 6: {'2'}})


defaultdict(<class 'set'>, {(0, 0): {'6', '9', '8', '3', '5'}, (0, 1): {'7', '1', '9', '5'}, (0, 2): {'6'}, (1, 0): {'8', '7', '4'}, (1, 1): {'6', '2', '3', '8'}, (1, 2): {'6', '1', '3'}, (2, 0): {'6'}, (2, 2): {'2', '8'}, (2, 1): {'4', '1', '9'}})


. 7 6
. 7 7
5 7 8


defaultdict(<class 'set'>, {0: {'7', '3', '5'}, 1: {'6', '1', '9', '5'}, 2: {'8', '6', '9'}, 3: {'8', '6', '3'}, 4: {'8', '4', '1', '3'}, 5: {'2', '7', '6'}, 6: {'6', '2', '8'}, 7: {'4', '1', '9', '5'}})


defaultdict(<class 'set'>, {0: {'6', '7', '8', '4', '5'}, 1: {'6', '9', '3'}, 4: {'6', '1', '9', '7', '2'}, 3: {'8', '4', '1'}, 5: {'9', '3', '5'}, 2: {'8'}, 7: {'6', '8'}, 8: {'6', '1', '3', '5'}, 6: {'2'}})


defaultdict(<class 'set'>, {(0, 0): {'6', '9', '8', '3', '5'}, (0, 1): {'7', '1', '9', '5'}, (0, 2): {'6'}, (1, 0): {'8', '7', '4'}, (1, 1): {'6', '2', '3', '8'}, (1, 2): {'6', '1', '3'}, (2, 0): {'6'}, (2, 2): {'2', '8', '5'}, (2, 1): {'4', '1', '9'}})


. 8 0
. 8 1
. 8 2
. 8 3
8 8 4


defaultdict(<class 'set'>, {0: {'7', '3', '5'}, 1: {'6', '1', '9', '5'}, 2: {'8', '6', '9'}, 3: {'8', '6', '3'}, 4: {'8', '4', '1', '3'}, 5: {'2', '7', '6'}, 6: {'6', '2', '8'}, 7: {'4', '1', '9', '5'}, 8: {'8'}})


defaultdict(<class 'set'>, {0: {'6', '7', '8', '4', '5'}, 1: {'6', '9', '3'}, 4: {'6', '1', '9', '7', '8', '2'}, 3: {'8', '4', '1'}, 5: {'9', '3', '5'}, 2: {'8'}, 7: {'6', '8'}, 8: {'6', '1', '3', '5'}, 6: {'2'}})


defaultdict(<class 'set'>, {(0, 0): {'6', '9', '8', '3', '5'}, (0, 1): {'7', '1', '9', '5'}, (0, 2): {'6'}, (1, 0): {'8', '7', '4'}, (1, 1): {'6', '2', '3', '8'}, (1, 2): {'6', '1', '3'}, (2, 0): {'6'}, (2, 2): {'2', '8', '5'}, (2, 1): {'8', '4', '1', '9'}})


. 8 5
. 8 6
7 8 7


defaultdict(<class 'set'>, {0: {'7', '3', '5'}, 1: {'6', '1', '9', '5'}, 2: {'8', '6', '9'}, 3: {'8', '6', '3'}, 4: {'8', '4', '1', '3'}, 5: {'2', '7', '6'}, 6: {'6', '2', '8'}, 7: {'4', '1', '9', '5'}, 8: {'8', '7'}})


defaultdict(<class 'set'>, {0: {'6', '7', '8', '4', '5'}, 1: {'6', '9', '3'}, 4: {'6', '1', '9', '7', '8', '2'}, 3: {'8', '4', '1'}, 5: {'9', '3', '5'}, 2: {'8'}, 7: {'6', '7', '8'}, 8: {'6', '1', '3', '5'}, 6: {'2'}})


defaultdict(<class 'set'>, {(0, 0): {'6', '9', '8', '3', '5'}, (0, 1): {'7', '1', '9', '5'}, (0, 2): {'6'}, (1, 0): {'8', '7', '4'}, (1, 1): {'6', '2', '3', '8'}, (1, 2): {'6', '1', '3'}, (2, 0): {'6'}, (2, 2): {'2', '7', '8', '5'}, (2, 1): {'8', '4', '1', '9'}})


9 8 8


defaultdict(<class 'set'>, {0: {'7', '3', '5'}, 1: {'6', '1', '9', '5'}, 2: {'8', '6', '9'}, 3: {'8', '6', '3'}, 4: {'8', '4', '1', '3'}, 5: {'2', '7', '6'}, 6: {'6', '2', '8'}, 7: {'4', '1', '9', '5'}, 8: {'8', '7', '9'}})


defaultdict(<class 'set'>, {0: {'6', '7', '8', '4', '5'}, 1: {'6', '9', '3'}, 4: {'6', '1', '9', '7', '8', '2'}, 3: {'8', '4', '1'}, 5: {'9', '3', '5'}, 2: {'8'}, 7: {'6', '7', '8'}, 8: {'6', '1', '9', '3', '5'}, 6: {'2'}})


defaultdict(<class 'set'>, {(0, 0): {'6', '9', '8', '3', '5'}, (0, 1): {'7', '1', '9', '5'}, (0, 2): {'6'}, (1, 0): {'8', '7', '4'}, (1, 1): {'6', '2', '3', '8'}, (1, 2): {'6', '1', '3'}, (2, 0): {'6'}, (2, 2): {'9', '7', '8', '2', '5'}, (2, 1): {'8', '4', '1', '9'}})


"""    