#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/2 上午11:34
# @Title   : 169. 多数元素
# @Link    : https://leetcode-cn.com/problems/majority-element/


QUESTION = """
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1:
输入: [3,2,3]
输出: 3

示例 2:
输入: [2,2,1,1,1,2,2]
输出: 2
"""


THINKING = """
排序之后，出现次数多的，肯定会在中位数位置出现
"""


from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]


if __name__ == '__main__':
    s = Solution()
    nums = [2,2,1,1,1,2,2]
    print(s.majorityElement(nums))
