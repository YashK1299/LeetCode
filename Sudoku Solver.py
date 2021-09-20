"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

 

Example 1:


Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:


 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.

"""


class Solution:
    
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def backtrack(i, j):
            if i==9:
                return True
            if board[i][j] != ".":
                return backtrack(i+j//8, (j+1)%9)
            for k in range(1, 10):
                if is_safe(i, j, k):
                    add_num(i, j, k)
                    if backtrack(i+j//8, (j+1)%9):
                        return True
                    remove_num(i, j, k)
            return False

        def is_safe(i, j, k):
            k = str(k)
            if k in row[i] or k in col[j] or k in box[(i-i%3,j-j%3)]:
                return False
            return True
        
        def add_num(i, j, k):
            k = str(k)
            board[i][j] = k
            row[i].add(k)
            col[j].add(k)
            box[(i-i%3, j-j%3)].add(k)
            
        def remove_num(i, j, k):
            k = str(k)
            board[i][j] = "."
            row[i].remove(k)
            col[j].remove(k)
            box[(i-i%3, j-j%3)].remove(k)
                
        row = [set() for i in range(9)]
        col = [set() for i in range(9)]
        box = dict()
        for i in range(9):
            for j in range(9):
                k = board[i][j]
                if k != ".":
                    row[i].add(k)
                    col[j].add(k)
                    if (i-i%3,j-j%3) in box:
                        box[(i-i%3,j-j%3)].add(k)
                    else:
                        box[(i-i%3,j-j%3)] = set(k)
                elif (i-i%3,j-j%3) not in box:
                    box[(i-i%3,j-j%3)] = set()
        backtrack(0, 0)
        return board