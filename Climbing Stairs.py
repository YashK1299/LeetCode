"""
    You are climbing a staircase. It takes n steps to reach the top.
    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

    Example 1:
        Input: n = 2
        Output: 2
        Explanation: There are two ways to climb to the top.
        1. 1 step + 1 step
        2. 2 steps

    Example 2:
        Input: n = 3
        Output: 3
        Explanation: There are three ways to climb to the top.
        1. 1 step + 1 step + 1 step
        2. 1 step + 2 steps
        3. 2 steps + 1 step

    Constraints:
        1 <= n <= 45
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        """
            Dynamic Programming using memoization and iteration:
                T(n) = O(n)
                S(n) = O(n)
        """
        if n == 0 or n == 1:
            return n
        c = [0]*n
        c[0] = 1
        c[1] = 2
        for i in range(2,n):
            c[i] = c[i-1] + c[i-2]
        return c[-1]
        """
            Using golden ratio:
                T(n) = O(log n)
                S(n) = O(1)
        """
        t = (1 + 5 ** 0.5) / 2
        p = (1 - 5 ** 0.5) / 2
        n+=1
        return int((t**n - p**n)/5**0.5)