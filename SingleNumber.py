#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/1 下午9:38
# @Title   : 136. 只出现一次的数字
# @Link    : https://leetcode-cn.com/problems/single-number/


QUESTION = """
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:
输入: [2,2,1]
输出: 1

示例 2:
输入: [4,1,2,1,2]
输出: 4
"""


THINKING = """
异或运算即是二进制每一位进行比较
如果相同则是0，不同则是1，所以只需要初始化一个值0，一个一个的运算下去
相同的数字会为0，剩下的内个就是出现一次的数字
没常接触过位运算的想不出来个人觉得也正常，一会知道了就完全ok
"""


from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        current = 0
        for i in nums:
            current = current ^ i
        return current


if __name__ == '__main__':
    s = Solution()
    nums = [2,2,1]
    print(s.singleNumber(nums))
