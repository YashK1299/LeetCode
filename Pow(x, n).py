"""
    Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

    Example 1:
        Input: x = 2.00000, n = 10
        Output: 1024.00000

    Example 2:
        Input: x = 2.10000, n = 3
        Output: 9.26100

    Example 3:
        Input: x = 2.00000, n = -2
        Output: 0.25000
        Explanation: 2-2 = 1/22 = 1/4 = 0.25

    Constraints:
        -100.0 < x < 100.0
        -2^31 <= n <= 2^31-1
        -10^4 <= x^n <= 10^4
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        # if n == 0:
        #     return 1
        # if n == 1:
        #     return x
        # if n < 0:
        #     n = -n
        #     x = 1/x
        # return x*self.myPow(x,n-1)
        """
            Using multiplication technique:
                T(n) = O(log(n))
                S(n) = O(1)
        """
        #         if n == 0:
        #             return 1
        #         if n == 1:
        #             return x
        #         if n == -1:
        #             return 1/x

        #         res = self.myPow(x, n//2)
        #         return res * res if n%2 == 0 else x * res * res
        """
            Using math.pow():
                T(n) = O(log(n))
                S(n) = O(1)
        """
        return pow(x, n)
