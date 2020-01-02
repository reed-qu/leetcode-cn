#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/2 上午11:25
# @Title   : 168. Excel表列名称
# @Link    : https://leetcode-cn.com/problems/excel-sheet-column-title/


QUESTION = """
给定一个正整数，返回它在 Excel 表中相对应的列名称。

例如，

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
    
示例 1:
输入: 1
输出: "A"

示例 2:
输入: 28
输出: "AB"

示例 3:
输入: 701
输出: "ZY"
"""


THINKING = """
大写字母A的ascii码为65，一直到Z是90，所以可以利用这一规律来实现

n % 26 为表示第几个字符，然后+65，则是找到对应的ascii码，然后通过chr内置函数，来转成字符拼接到result上
直到整除26为0
"""


class Solution:
    def convertToTitle(self, n: int) -> str:
        result = ""
        while (n):
            n -= 1
            result = chr(n % 26 + 65) + result
            n = n // 26
        return result


if __name__ == '__main__':
    s = Solution()
    n = 702
    print(s.convertToTitle(n))
