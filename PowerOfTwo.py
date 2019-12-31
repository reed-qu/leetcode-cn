#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/17 下午4:59
# @Title   : 231. 2的幂
# @Link    : https://leetcode-cn.com/problems/power-of-two/


QUESTION = """
给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

示例 1:
输入: 1
输出: true
解释: 20 = 1

示例 2:
输入: 16
输出: true
解释: 24 = 16

示例 3:
输入: 218
输出: false
"""


THINKING = """
这种问题的思路效率最高的就是用二进制来考虑
首先2的n次幂的二进制首位是1，其后位全是0
且2的n次幂-1的二进制就是首位是0(如果对齐的话)，其后位全是1，所以直接进行位与运行就可以了，为0即可

考虑不允许为负数
"""


class Solution(object):
    def isPowerOfTwo(self, n: int) -> int:
        return n > 0 and n & (n-1) == 0


if __name__ == '__main__':
    s = Solution()
    n = 218
    print(s.isPowerOfTwo(n))
