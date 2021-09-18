"""
    Given an encoded string, return its decoded string.
    The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is
    being repeated exactly k times. Note that k is guaranteed to be a positive integer.
    You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
    Furthermore, you may assume that the original data does not contain any digits and that digits
    are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

    Example 1:
        Input: s = "3[a]2[bc]"
        Output: "aaabcbc"

    Example 2:
        Input: s = "3[a2[c]]"
        Output: "accaccacc"

    Example 3:
        Input: s = "2[abc]3[cd]ef"
        Output: "abcabccdcdcdef"

    Example 4:
        Input: s = "abc3[cd]xyz"
        Output: "abccdcdcdxyz"

    Constraints:
        1 <= s.length <= 30
        s consists of lowercase English letters, digits, and square brackets '[]'.
        s is guaranteed to be a valid input.
        All the integers in s are in the range [1, 300].
"""


class Solution:
    #     def decodeString(self, s: str) -> str:

    #         def dfs(i):
    #             string = ""
    #             num = ""
    #             while i < len(s):
    #                 if s[i].isnumeric():
    #                     num = num + s[i]
    #                     i += 1
    #                 elif s[i] == '[':
    #                     temp, i = dfs(i+1)
    #                     string += temp * int(num)
    #                     num = ""
    #                 elif s[i] == ']':
    #                     return (string, i+1)
    #                 else:
    #                     string += s[i]
    #                     i += 1
    #             return string

    #         return dfs(0)

    def decodeString(self, s: str) -> str:
        stack = []
        res = ""
        num = ""

        for i in s:
            if i.isdigit():
                num += i
            elif i == '[':
                stack.append([res, num])
                num, res = "", ""
                # res = ""
            elif i == ']':
                prevs, prevn = stack.pop()
                res = prevs + res * int(prevn)
            else:
                res += i
        return res

#     def decodeString(self, s: str) -> str:
#         stack = []
#         for i in s:
#             if i == ']':
#                 res = ""
#                 while stack:
#                     temp = stack.pop()
#                     if temp == '[':
#                         break
#                     res = temp + res
#                 num = ''
#                 while stack and stack[-1].isdigit():
#                     num = stack.pop() + num
#                 stack.append(res*int(num))
#             else:
#                 stack.append(i)
#         return ''.join(stack)
