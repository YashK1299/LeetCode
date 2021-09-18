"""
    Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

    Example 1:
        Input: n = 3
        Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

    Example 2:
        Input: n = 1
        Output: [[1]]

    Constraints:
        1 <= n <= 8
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        nums = list(range(1, n + 1))

        def rec(l):
            if len(l) == 0:
                return [None]
            if len(l) == 1:
                return [TreeNode(l[0])]
            res = []
            for i in range(len(l)):
                ls = rec(l[:i])
                rs = rec(l[i + 1:])
                for j in ls:
                    for k in rs:
                        res.append(TreeNode(l[i], j, k))
            return res

        return rec(nums)
