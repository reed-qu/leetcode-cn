#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/30 下午5:11
# @Title   : 1. 两数之和
# @Link    : https://leetcode-cn.com/problems/two-sum/


QUESTION = """
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""


THINKING = """
因为这里假设只有一个答案，不会重复，所以思路自然就想到应用到哈希表
哈希表里记录的是{value: index}，即数组中的值对应的索引index
这样从头开始遍历数组的时候，每次为了计算出了两个数字之和为target，则每次判断的是(target-当前数字)在哈希表中是否存在
如果存在则表示 target - 当前数字 = 哈希表中已存在的数字，那么答案就出来了，就是[当前数字的索引, 哈希表中已存在的数字的索引]
"""


from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_to_index = {}

        for index, value in enumerate(nums):
            exist_index = value_to_index.get(target - value)
            if exist_index is not None:
                return [exist_index, index]

            value_to_index[value] = index


if __name__ == '__main__':
    s = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(s.twoSum(nums, target))
