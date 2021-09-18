"""
    Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
    return the number of islands.
    An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
    You may assume all four edges of the grid are all surrounded by water.

    Example 1:
        Input: grid = [
          ["1","1","1","1","0"],
          ["1","1","0","1","0"],
          ["1","1","0","0","0"],
          ["0","0","0","0","0"]
        ]
        Output: 1

    Example 2:
        Input: grid = [
          ["1","1","0","0","0"],
          ["1","1","0","0","0"],
          ["0","0","1","0","0"],
          ["0","0","0","1","1"]
        ]
        Output: 3

    Constraints:
        m == grid.length
        n == grid[i].length
        1 <= m, n <= 300
        grid[i][j] is '0' or '1'.
"""
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
            DFS Approach:
                T(n) = O(n^2)
                S(n) = O(n^2)
        """
        m = len(grid)
        n = len(grid[0])
        count = 0
        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        def validNeighbour(i, j):
            if i<0 or j<0 or i == m or j == n:
                return False
            if grid[i][j] != '1':
                return False
            return True

        def dfs(i,j):
            stack = [(i,j)]
            while stack:
                p, q = stack.pop()
                for each in directions:
                    newp = p + each[0]
                    newq = q + each[1]
                    if validNeighbour(newp, newq):
                        stack.append((newp, newq))
                        grid[newp][newq] = 'V'

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i,j)
                    grid[i][j] = 'V'
                    count += 1
        return count

#         """
#             BFS Approach without using visited Set:
#                 T(n) = O(n)
#                 S(n) = O(n)
#         """
#         m = len(grid)
#         n = len(grid[0])
#         count = 0
#         directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#
#         def validNeighbour(i, j):
#             if i < 0 or j < 0 or i == m or j == n:
#                 return False
#             if grid[i][j] != '1':
#                 return False
#             return True
#
#         def bfs(i, j):
#             queue = deque([(i, j)])
#             while queue:
#                 p, q = queue.popleft()
#                 for each in directions:
#                     newp = p + each[0]
#                     newq = q + each[1]
#                     if validNeighbour(newp, newq):
#                         queue.append((newp, newq))
#                         grid[newp][newq] = 'V'
#
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == '1':
#                     bfs(i, j)
#                     grid[i][j] = 'V'
#                     count += 1
#         return count
        
#         """
#             BFS Approach:
#                 T(n) = O(n^2)
#                 S(n) = O(n^2)
#         """
#         queue = deque()
#         visited = set()
#         count = 0
#         for m in range(len(grid)):
#             for n in range(len(grid[m])):
#                 if ((m,n) not in visited) and (grid[m][n] == "1"):
#                     queue.append([m,n])
#                     count += 1
#                 visited.add((m,n))
#                 while queue:
#                     i, j = queue.popleft()

#                     if i > 0 and (i-1,j) not in visited and grid[i-1][j] == "1":
#                         queue.append((i-1,j))
#                         visited.add((i-1,j))

#                     if i < len(grid) - 1 and (i+1,j) not in visited and grid[i+1][j] == "1":
#                         queue.append((i+1,j))
#                         visited.add((i+1,j))

#                     if j > 0 and (i,j-1) not in visited and grid[i][j-1] == "1":
#                         queue.append((i,j-1))
#                         visited.add((i,j-1))

#                     if j < len(grid[0])-1 and (i,j+1) not in visited and grid[i][j+1] == "1":
#                         queue.append((i,j+1))
#                         visited.add((i,j+1))

#         return count
