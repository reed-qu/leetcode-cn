#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/8 下午3:03
# @Title   : 215. 数组中的第K个最大元素
# @Link    : https://leetcode-cn.com/problems/kth-largest-element-in-an-array/
# TODO     : 快速选择算法


QUESTION = """
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:
输入: [3,2,1,5,6,4] 和 k = 2
输出: 5

示例 2:
输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4

说明:
你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
"""

THINKING = """
1. heapq模块的nlargest方法，返回的就是数组中前k大的数组
2. 引入字典计数，然后排序找
3. 快速选择算法[https://en.wikipedia.org/wiki/Quickselect] 太复杂没看
"""


from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]


if __name__ == '__main__':
    s = Solution()
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    print(s.findKthLargest(nums, k))
