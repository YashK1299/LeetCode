"""
    An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.
    You are also given three integers sr, sc, and newColor.
    You should perform a flood fill on the image starting from the pixel image[sr][sc].
    To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the
    starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those
    pixels (also with the same color), and so on.
    Replace the color of all of the aforementioned pixels with newColor.
    Return the modified image after performing the flood fill.

    Example 1:
        Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
        Output: [[2,2,2],[2,2,0],[2,0,1]]
        Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel),
                     all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels)
                     are colored with the new color.
                     Note the bottom corner is not colored 2, because it is not 4-directionally connected
                     to the starting pixel.

    Example 2:
        Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2
        Output: [[2,2,2],[2,2,2]]

    Constraints:
        m == image.length
        n == image[i].length
        1 <= m, n <= 50
        0 <= image[i][j], newColor < 216
        0 <= sr < m
        0 <= sc < n
"""


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        """
            DFS using stacks:
                T(n) = O(n)
                S(n) = O(n)
        """
        stack = [(sr, sc)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n = len(image), len(image[0])
        color = image[sr][sc]

        if color == newColor:
            return image

        def validNeighbor(r, c):
            if r < 0 or c < 0 or r > m - 1 or c > n - 1:
                return False
            if image[r][c] != color:
                return False
            return True

        while stack:
            i, j = stack.pop(0)
            image[i][j] = newColor
            for a, b in directions:
                if validNeighbor(i + a, j + b): stack.append((i + a, j + b))

        return image

#         """
#             DFS without stacks:
#                 T(n) = O(n)
#                 S(n) = O(n)
#         """
#         m, n = len(image), len(image[0])
#         color = image[sr][sc]
#         directions = [(0,1),(1,0),(0,-1),(-1,0)]

#         if color == newColor: return image

#         def validNeighbor(r,c):
#             return False if (r<0 or c<0 or r>m-1 or c>n-1) else True

#         def dfs(i, j):
#             if image[i][j] == color:
#                 image[i][j] = newColor
#                 for p, q in directions:
#                     if validNeighbor(i+p, j+q): dfs(i+p, j+q)

#         dfs(sr, sc)
#         return image
