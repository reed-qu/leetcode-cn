#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/30 下午2:54
# @Title   : 35. 搜索插入位置
# @Link    : https://leetcode-cn.com/problems/search-insert-position/


QUESTION = """
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引
如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
你可以假设数组中无重复元素。

示例 1:
输入: [1,3,5,6], 5
输出: 2

示例 2:
输入: [1,3,5,6], 2
输出: 1

示例 3:
输入: [1,3,5,6], 7
输出: 4

示例 4:
输入: [1,3,5,6], 0
输出: 0
"""


THINKING = """
有序数组这种查找一般是二分查找
思路是，左右各创建一个指针left, right，每次判断中间(left + (right - left) // 2)的数字和target的大小关系
如果小于target则重新设置left为mid+1，如果大于或等于target则重新设置right为mid
同时当left>=right时则停止循环，返回left
"""


from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0

        l = len(nums)
        left, right = 0, l
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 14]
    target = 13
    print(s.searchInsert(nums, target))
