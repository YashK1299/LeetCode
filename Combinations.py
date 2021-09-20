"""
Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.

 

Example 1:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
Example 2:

Input: n = 1, k = 1
Output: [[1]]
 

Constraints:

1 <= n <= 20
1 <= k <= n
"""


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n < k:
            return False
        if k==0:
            return [[]]
        ans = []
        for i in range(n, k-1, -1):
            temp = self.combine(i-1, k-1)
            if temp:
                for j in temp:
                    ans += [[i] + j]
        return ans