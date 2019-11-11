#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/11 下午4:18
# @Title   : 69. x 的平方根
# @Link    : https://leetcode-cn.com/problems/sqrtx/


QUESTION = """
实现 int sqrt(int x) 函数。
计算并返回 x 的平方根，其中 x 是非负整数。
由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:
输入: 4
输出: 2

示例 2:
输入: 8
输出: 2

说明: 8 的平方根是 2.82842..., 
     由于返回类型是整数，小数部分将被舍去。
"""


THINKING = """
典型的牛顿迭代法近似求解问题，做机器学习的基本上是必须要了解的
求解平方根，可以令 y = x^2 - a，求解x，比如要求解x^2=8，即可令x^2-8=0来求解x

1. x_k点的切线为
    f'(x_k)= (y - f(x_k)) / (x - x_k) = 2x
2. 令y=0即是x的解，即
    x = x_k - f(x_k) / f'(x_k)
3. 求导数，和已知公式
    f'(x_k) = 2x_k
    f(x_k) = x_k^2 - a
4. 于是有
    x = x_k - (x_k^2 - a) / 2x_k
    x = (x_k^2 + a) / 2x_k
    x = (x_k + a / x_k) / 2
5. 给x_k一个初始值init，比如 x_k = init = 1，开始迭代
6. 如果x_k 与 x相差小于一个很小的数字，比如是1e-4，就可以认为x为所求的解，否则把此轮的值x作为init继续迭代，直到收敛
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        threshold = 1e-4
        init = 1
        while 1:
            current = (init + x / init) / 2
            if abs(current - init) < threshold:
                return int(current)
            else:
                init = current


if __name__ == '__main__':
    s = Solution()
    x = 2
    print(s.mySqrt(x))
