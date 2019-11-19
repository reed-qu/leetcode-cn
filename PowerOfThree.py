#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/19 上午10:31
# @Title   : 326. 3的幂
# @Link    : https://leetcode-cn.com/problems/power-of-three/


QUESTION = """
给定一个整数，写一个函数来判断它是否是 3 的幂次方。

示例 1:
输入: 27
输出: true

示例 2:
输入: 0
输出: false

示例 3:
输入: 9
输出: true

示例 4:
输入: 45
输出: false

进阶：
你能不使用循环或者递归来完成本题吗？
"""


THINKING = """
int类型在正数上最大的数字为 (1<<31) - 1
遍历出来所有在int范围内的所有3的n次幂数，查找是不是在其中之内就可以了
思路就是指数增长的速度特别快，所以一共也不会有太多的数字，穷举很容易
"""


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        valid_n = [1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147,
                   531441, 1594323, 4782969, 14348907, 43046721, 129140163,
                   387420489, 1162261467]
        if n in valid_n:
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    n = 127
    print(s.isPowerOfThree(n))
