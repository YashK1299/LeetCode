"""
    Given an integer n, return the least number of perfect square numbers that sum to n.
    A perfect square is an integer that is the square of an integer; in other words,
    it is the product of some integer with itself.
    For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

    Example 1:
        Input: n = 12
        Output: 3
        Explanation: 12 = 4 + 4 + 4.

    Example 2:
        Input: n = 13
        Output: 2
        Explanation: 13 = 4 + 9.

    Constraints:
        1 <= n <= 104
"""


class Solution:
    def numSquares(self, n: int) -> int:
        """
            DP Approach: for some reason gives TLE sometimes
                T(n) = O(n^(3/2))
                S(n) = O(n)
        """
        res = [0, 1, 2, 3]
        for i in range(4, n + 1):
            res.append(math.inf)
            for j in range(1, floor(i ** 0.5) + 1):
                res[i] = min(res[i], 1 + res[i - j ** 2])
        return res[n]
        # """
        #     BFS Approach:
        #         T(n) = O(n^(3/2))
        #         S(n) = O(n)
        # """
        # queue = deque([(0, 0)])
        # seen = set()
        # while queue:
        #     i, step = queue.popleft()
        #     for j in range(1, floor(n ** 0.5) + 1):
        #         s = i + j ** 2
        #         if s == n:
        #             return step + 1
        #         if s not in seen:
        #             queue.append((s, step + 1))
        #             seen.add(s)
