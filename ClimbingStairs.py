#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/11 下午10:09
# @Title   : 70. 爬楼梯
# @Link    : https://leetcode-cn.com/problems/climbing-stairs/


QUESTION = """
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。

示例 1：
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶

示例 2：
输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
"""


THINKING = """
本题是一个动态规划问题，因为每一步可以迈1或者2步
公式为 dp[i] = dp[i-1] + dp[i-2]
其实解释起来就是第i阶的步数等于前一阶 + 前两阶的和
比如1阶->1种；2阶->2种；3阶->3种；4阶->5种；这很明显是一个斐波那契数列
所以我们只需要实现斐波那契额数列就可以了
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a+b
        return b


if __name__ == '__main__':
    s = Solution()
    n = 4
    print(s.climbStairs(n))
