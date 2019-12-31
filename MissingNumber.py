#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/18 上午9:45
# @Title   : 268. 缺失数字
# @Link    : https://leetcode-cn.com/problems/missing-number/


QUESTION = """
给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数

示例 1:
输入: [3,0,1]
输出: 2

示例 2:
输入: [9,6,4,2,3,5,7,0,1]
输出: 8

说明:
你的算法应具有线性时间复杂度。你能否仅使用额外常数空间来实现?
"""


THINKING = """
一个序列，里面缺失且只缺失1个数字，那么就可以用求和公式来进行差运算，即可求出来少的内个数字
高斯求和公式计算0..n的和为formula_sum
列表里面的数字总和为loop_sum
缺失的数字也就是formula_sum - loop_sum

这里用数学的方式来处理就很简单
"""


from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        formula_sum = int(len(nums) * (len(nums)+1) / 2)
        loop_sum = sum(nums)
        return formula_sum - loop_sum


if __name__ == '__main__':
    s = Solution()
    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    print(s.missingNumber(nums))
