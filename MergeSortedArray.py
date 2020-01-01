#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/1 下午10:26
# @Title   : 88. 合并两个有序数组
# @Link    : https://leetcode-cn.com/problems/merge-sorted-array/


QUESTION = """
给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。

示例:
输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3
输出: [1,2,2,3,5,6]
"""


THINKING = """
原地修改nums1即可，根据题设直写即可
"""


from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        nums1[m:] = nums2
        nums1.sort()
        return nums1


if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    print(s.merge(nums1, m, nums2, n))
