"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
"""


# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         if needle is not str:
#             return 0
#         if len(needle) > len(haystack):
#             return -1
#         i, j = 0, 0
#         index = [-1]
#         while i < len(needle) and j < len(haystack):
#             if needle[i] == haystack[j]:
#                 index.append(j)
#                 i = i + 1
#                 j = j + 1
#             else:
#                 j = j + 1
#         return index[0]

# TODO 别人解法 太强了
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i: i + len(needle)] == needle:
                return i

        return -1


