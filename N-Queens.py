"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

Example 1:


Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]
 

Constraints:

1 <= n <= 9
"""


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # board = [["." for i in range(n)] for j in range(n)]
        # self.ans = []
        # self.countQueens(board, 0)
        # return self.ans
        
        def countQ(i):
            nonlocal ans
            if i == n:
                ans += [["".join(x) for x in board]]
                return
            for j in range(n):
                if not col[j] and not diagonal[i+j] and not antidiagonal[i-j]:
                    board[i][j] = "Q"
                    col[j] = True
                    diagonal[i+j] = True
                    antidiagonal[i-j] = True
                    countQ(i+1)
                    board[i][j] = "."
                    col[j] = False
                    diagonal[i+j] = False
                    antidiagonal[i-j] = False
        
        board = [["." for i in range(n)] for j in range(n)]
        ans = []
        col = [False for i in range(n)]
        diagonal = defaultdict(bool)
        antidiagonal = defaultdict(bool)
        countQ(0)
        return ans
        
    def countQueens(self, board, i):
        if i == len(board):
            self.ans += [["".join(x) for x in board]]
            return 
        for j in range(len(board[0])):
            if self.safe(board, i, j):
                board[i][j] = "Q"
                c = self.countQueens(board, i+1)
                board[i][j] = "."
        
    def safe(self, board, i, j):
        for m in range(i):
            if board[m][j] == "Q":
                return False
        m, n = i, j
        while m > 0 and n > 0:
            m-=1
            n-=1
            if board[m][n] == "Q":
                return False
        m, n = i, j
        while n < len(board[0])-1 and m >= 0:
            m-=1
            n+=1
            if board[m][n] == "Q":
                return False
        return True
        