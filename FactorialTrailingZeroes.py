#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/2 下午12:03
# @Title   : 172. 阶乘后的零
# @Link    : https://leetcode-cn.com/problems/factorial-trailing-zeroes/


QUESTION = """
给定一个整数 n，返回 n! 结果尾数中零的数量。

示例 1:
输入: 3
输出: 0
解释: 3! = 6, 尾数中没有零。

示例 2:
输入: 5
输出: 1
解释: 5! = 120, 尾数中有 1 个零.

说明: 你算法的时间复杂度应为 O(log n) 。
"""


THINKING = """
位数中有没有零，主要是看取决于哪些数字
经过举例和思考，其实容易发现，其实就是看n是5的几倍
其中包含1个5，就会有1个0，这样一来问题就迎刃而解了
"""


class Solution:
    def trailingZeroes(self, n: int) -> int:
        result = 0
        while n >= 5:
            result += n // 5
            n //= 5
        return result


if __name__ == '__main__':
    s = Solution()
    n = 15
    print(s.trailingZeroes(n))
