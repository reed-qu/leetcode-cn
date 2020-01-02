#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/2 上午11:40
# @Title   : 171. Excel表列序号
# @Link    : https://leetcode-cn.com/problems/excel-sheet-column-number/


QUESTION = """
给定一个Excel表格中的列名称，返回其相应的列序号。

例如，

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
    
示例 1:
输入: "A"
输出: 1

示例 2:
输入: "AB"
输出: 28

示例 3:
输入: "ZY"
输出: 701
"""


THINKING = """
与从数字转成EXCEL列名的问题相似
从最后一位开始往前处理，也是应用ascii码的特性，注意这里有个 26**i 的因子
"""


class Solution:
    def titleToNumber(self, s: str) -> int:
        result = 0
        for i, s in enumerate(s[::-1]):
            result += (ord(s)-64) * (26**i)
        return result


if __name__ == '__main__':
    s = Solution()
    string = "ZY"
    print(s.titleToNumber(string))
