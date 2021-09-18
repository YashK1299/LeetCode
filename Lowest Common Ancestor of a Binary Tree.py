"""
    Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
    According to the definition of LCA on Wikipedia:
        “The lowest common ancestor is defined between two nodes p and q as the lowest node in T
        that has both p and q as descendants (where we allow a node to be a descendant of itself).”

    Example 1:
        Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
        Output: 3
        Explanation: The LCA of nodes 5 and 1 is 3.

    Example 2:
        Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
        Output: 5
        Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

    Example 3:
        Input: root = [1,2], p = 1, q = 2
        Output: 1

    Constraints:
        The number of nodes in the tree is in the range [2, 10^5].
        -10^9 <= Node.val <= 10^9
        All Node.val are unique.
        p != q
        p and q will exist in the tree.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
            DFS Recursive approach:
                T(n) = O(n)
                S(n) = O(log(n))
        """
        if not root:
            return None

        res1 = self.lowestCommonAncestor(root.left, p, q)
        res2 = self.lowestCommonAncestor(root.right, p, q)
        if (res1 and res2) or (root == p or root == q):
            return root
        else:
            return res1 or res2

    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
            Using parent pointers: Save parent pointers for each node
            Save all of p's ancestors in a set
            Check for each ancestor of q if it is in the set or not
            The first ancestor in the set is the lowest common ancestor
                T(n) = O(n)
                S(n) = O(n)
        """
        stack = [root]
        parent = {root: None}
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]
        while q not in ancestors:
            q = parent[q]
        return q
