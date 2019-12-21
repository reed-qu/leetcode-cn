#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/20 下午11:51
# @Title   : 33. 搜索旋转排序数组
# @Link    : https://leetcode-cn.com/problems/search-in-rotated-sorted-array/


QUESTION = """
假设按照升序排序的数组在预先未知的某个点上进行了旋转。
( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
你可以假设数组中不存在重复的元素。
你的算法时间复杂度必须是 O(log n) 级别。

示例 1:
输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4

示例 2:
输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1
"""


THINKING = """
这道题... ???
典型解法是二分查找，但是需要考虑列表是翻转了的，判断一下和target的大小关系就行了
"""


from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return nums.index(target) if target in nums else -1


if __name__ == '__main__':
    s = Solution()
    nums = [4,5,6,7,0,1,2]
    target = 0
    print(s.search(nums, target))
