"""
    Reverse String: Write a function that reverses a string. The input string is given as an array of characters s.

    Example 1:
        Input: s = ["h","e","l","l","o"]
        Output: ["o","l","l","e","h"]

    Example 2:
        Input: s = ["H","a","n","n","a","h"]
        Output: ["h","a","n","n","a","H"]

    Constraints:
        1 <= s.length <= 105
        s[i] is a printable ascii character.

    Follow up: Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
"""
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        """
            Recursive approach:
                T(n) = O(n)
                S(n) = O(n) recursive stack
        """
        def rec(low, high):
            if low < high:
                s[low], s[high] = s[high], s[low]
                rec(low+1, high -1)
        rec(0, len(s)-1)

        """
            Two pointer Approach:
                T(n) = O(n)
                S(n) = O(1)
        """
        low = 0
        high = len(s)-1
        while low < high:
            s[low], s[high] = s[high], s[low]
            low += 1
            high -= 1

        """
            Short Two pointer Approach:
                T(n) = O(n)
                S(n) = O(1)
        """
        for i in range(len(s) // 2):
            s[i], s[-1 - i] = s[-1 - i], s[i]

