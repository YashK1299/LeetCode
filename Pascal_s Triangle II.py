"""
    Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
    In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

    Example 1:
        Input: rowIndex = 3
        Output: [1,3,3,1]

    Example 2:
        Input: rowIndex = 0
        Output: [1]

    Example 3:
        Input: rowIndex = 1
        Output: [1,1]


    Constraints:
        0 <= rowIndex <= 33

    Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?
"""


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        """
            Using nCr formula one liner:
                T(n) = O(n)
                S(n) = O(n) for result
        """
        # return [comb(rowIndex, i) for i in range(rowIndex + 1)]
        """
            Optimized nCr usage: Logic nCr = nC(r-1) * (n-r+1) // r
                T(n) = O(n)
                S(n) = O(n) for result
        """
        res = [1]
        for i in range(1, rowIndex+1):
            res.append(res[-1] * (rowIndex - i + 1) // i)
        return res
