#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/12 下午2:16
# @Title   : 389. 找不同
# @Link    : https://leetcode-cn.com/problems/find-the-difference/


QUESTION = """
给定两个字符串 s 和 t，它们只包含小写字母。

字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。

请找出在 t 中被添加的字母。

示例:
输入：
s = "abcd"
t = "abcde"
输出：
e
解释：
'e' 是那个被添加的字母。
"""


THINKING = """
遍历可以实现，找出is not in s的内个即可，但是效率不高
题设中说了，只包含小写字母，而且只加了1个字符，那么就好办了，26个字符每一个都对应一个ASCII码
两个ASCII的和之差，就是多出来的内个字母了呗
"""


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(sum(map(ord, t)) - sum(map(ord, s)))


if __name__ == '__main__':
    sl = Solution()
    s = "abcd"
    t = "abcde"
    print(sl.findTheDifference(s, t))
