#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/1 下午2:56
# @Title   : 342. 4的幂
# @Link    : https://leetcode-cn.com/problems/power-of-four/


QUESTION = """
给定一个整数 (32 位有符号整数)，请编写一个函数来判断它是否是 4 的幂次方。

示例 1:
输入: 16
输出: true

示例 2:
输入: 5
输出: false

进阶：你能不使用循环或者递归来完成本题吗？
"""


THINKING = """
解决办法其实有很多，这里主要说2个比较简单易用的
前提条件是 num > 0

1. 穷举... 虽然很无脑，但也是一种不错的解决办法
2. 数学方法，x = 4 ^ a，a = log_4{x}，判断log_4{x}是不是整数就行了
"""


import math


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0:
            return False
        power_of = math.log(num, 4)
        return int(power_of) == power_of


if __name__ == '__main__':
    s = Solution()
    num = 16
    print(s.isPowerOfFour(num))
