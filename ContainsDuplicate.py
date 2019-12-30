#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/20 上午11:40
# @Title   : 217. 存在重复元素
# @Link    : https://leetcode-cn.com/problems/contains-duplicate/


QUESTION = """
给定一个整数数组，判断是否存在重复元素。
如果任何值在数组中出现至少两次，函数返回 true
如果数组中每个元素都不相同，则返回 false。

示例 1:
输入: [1,2,3,1]
输出: true

示例 2:
输入: [1,2,3,4]
输出: false

示例 3:
输入: [1,1,1,3,3,4,3,2,4,2]
输出: true
"""


THINKING = """
借助哈希表或者集合即可，更直接一点的可以len(nums) == len(set(nums))也行
"""


from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for each in nums:
            if each in s:
                return True
            else:
                s.add(each)
        return False


if __name__ == '__main__':
    s = Solution()
    nums = [1,1,1,3,3,4,3,2,4,2]
    print(s.containsDuplicate(nums))
