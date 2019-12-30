#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/20 下午2:25
# @Title   : 67. 二进制求和
# @Link    : https://leetcode-cn.com/problems/add-binary/


QUESTION = """
给定两个二进制字符串，返回他们的和（用二进制表示）
输入为非空字符串且只包含数字 1 和 0。

示例 1:
输入: a = "11", b = "1"
输出: "100"

示例 2:
输入: a = "1010", b = "1011"
输出: "10101"
"""


THINKING = """
对于Python来说很容易，跟着题设的思维来处理就可以了
内置的int, bin即可实现，速度也不错
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]


if __name__ == '__main__':
    s = Solution()
    a = "1010"
    b = "1011"
    print(s.addBinary(a, b))
