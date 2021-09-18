"""
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

    Example 1:
        Input: s = "()"
        Output: true

    Example 2:
        Input: s = "()[]{}"
        Output: true

    Example 3:
        Input: s = "(]"
        Output: false

    Example 4:
        Input: s = "([)]"
        Output: false

    Example 5:
        Input: s = "{[]}"
        Output: true

    Constraints:
        1 <= s.length <= 10^4
        s consists of parentheses only '()[]{}'.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        cl = {")":"(", "}":"{", "]":"["}
        for i in s:
            if i in cl.values():
                stack.append(i)
            elif not stack or stack.pop() != cl[i]:
                    return False
        return not stack
