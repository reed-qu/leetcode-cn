#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/28 下午5:27
# @Title   : 7. 整数反转
# @Link    : https://leetcode-cn.com/problems/reverse-integer/


QUESTION = """
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:
输入: 123
输出: 321

示例 2:
输入: -123
输出: -321

示例 3:
输入: 120
输出: 21

注意:
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
"""


THINKING = """
1. 首先Python3中的int范围是理论上无限的，所以这里引入数据边界[−2^31,  2^31 − 1]就可以了，每次比较一下大小判断是否溢出
2. 正负数只是符号的差别，所以都转化成正数来处理
3. 依次拿出数字的最后一位i( x % 10 )，然后将上一轮的结果result * 10 + i，初始result为0，这样第一轮的result即为i
4. 每一轮判断结果是否超过数据边界[−2^31,  2^31 − 1]，如果超过则return 0
5. 一轮结束后，数字x要缩小10倍
6. 最后通过参数x的符号，判断返回数字的符号

注意：Python3中向下取整为 //
"""


class Solution:
    def run(self, x: int) -> int:
        y , result = abs(x), 0
        threshold = (1 << 31) - 1 if x > 0 else 1 << 31
        while y != 0:
            i = y % 10
            result = result * 10 + i
            if result > threshold:
                return 0
            y = y // 10
        return result if x > 0 else -result


if __name__ == '__main__':
    s = Solution()
    print(s.run(-1050))
