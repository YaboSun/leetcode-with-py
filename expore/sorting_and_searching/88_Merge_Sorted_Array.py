"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]


Constraints:

-10^9 <= nums1[i], nums2[i] <= 10^9
nums1.length == m + n
nums2.length == n
"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        从后往前进行归并
        """
        i = m - 1
        j = n - 1
        tmp = len(nums1) - 1
        while i >= 0 and j >= 0:
            if nums2[j] >= nums1[i]:
                nums1[tmp] = nums2[j]
                tmp = tmp - 1
                j = j - 1
            else:
                nums1[tmp] = nums1[i]
                tmp = tmp - 1
                i = i - 1
        if j >= 0:
            nums1[:j + 1] = nums2[:j + 1]


if __name__ == '__main__':
    so = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]

    so.merge(nums1, nums2, 3, 3)
    print(nums1)
