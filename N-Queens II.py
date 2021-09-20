"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

 

Example 1:


Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
Example 2:

Input: n = 1
Output: 1
 

Constraints:

1 <= n <= 9

"""


class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [[0 for i in range(n)] for j in range(n)]
        # return self.countQueens(board, 0)
        
        def countQ(i):
            nonlocal ans
            if i == n:
                ans += 1
                return
            for j in range(n):
                if not col[j] and not diagonal[i+j] and not antidiagonal[i-j]:
                    board[i][j] = 1
                    col[j] = True
                    diagonal[i+j] = True
                    antidiagonal[i-j] = True
                    countQ(i+1)
                    board[i][j] = 0
                    col[j] = False
                    diagonal[i+j] = False
                    antidiagonal[i-j] = False
        
        ans = 0
        col = [False for i in range(n)]
        diagonal = defaultdict(bool)
        antidiagonal = defaultdict(bool)
        countQ(0)
        return ans
        
        self.ans = 0
        self.col = [False for i in range(n)]
        self.diagonal = defaultdict(bool)
        self.antidiagonal = defaultdict(bool)
        self.countQ(n, 0)
        return self.ans
        
    def countQueens(self, board, i):
        count = 0
        if i == len(board):
            return 1
        for j in range(len(board[0])):
            if self.safe(board, i, j):
                board[i][j] = 1
                c = self.countQueens(board, i+1)
                if c:
                    count += c
                board[i][j] = 0
        return count
        
    def safe(self, board, i, j):
        for m in range(i):
            if board[m][j] == 1:
                return False
        m, n = i, j
        while m > 0 and n > 0:
            m-=1
            n-=1
            if board[m][n] == 1:
                return False
        m, n = i, j
        while n < len(board[0])-1 and m >= 0:
            m-=1
            n+=1
            if board[m][n] == 1:
                return False
        return True
    
    def countQ(self, n, i):
        if i == n:
            self.ans += 1
            return
        for j in range(n):
            if not self.col[j] and not self.diagonal[i+j] and not self.antidiagonal[i-j]:
                self.col[j] = True
                self.diagonal[i+j] = True
                self.antidiagonal[i-j] = True
                
                self.countQ(n, i+1)
                
                self.col[j] = False
                self.diagonal[i+j] = False
                self.antidiagonal[i-j] = False
    